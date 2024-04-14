import subprocess
import zipfile
from pathlib import Path

import pandas as pd

FILENAME = "ml-1m"
MARKER = "_SUCCESS"


def load_data(path: str) -> None:
    print("Start loading MovieLens dataset...")

    local_path = Path(path).resolve()
    local_path.mkdir(parents=True, exist_ok=True)

    marker_path = str(local_path.joinpath(MARKER))

    if Path(marker_path).is_file() is True:
        print(f"MovieLens dataset already exists... at {path}")
        return

    try:
        zip_filename = f"{FILENAME}.zip"
        download_url = f"https://files.grouplens.org/datasets/movielens/{zip_filename}"
        subprocess.check_call(f"curl -o {path}/{zip_filename} {download_url}", shell=True)

        file_zip = zipfile.ZipFile(f"{path}/{zip_filename}")
        file_zip.extractall(local_path)

        ratings = pd.read_csv(
            f"{path}/{FILENAME}/ratings.dat",
            delimiter="::",
            names=["user_id", "movie_id", "rating", "timestamp"],
            engine="python",
            encoding="ISO-8859-1",
        )

        ratings.to_csv(f"{path}/ratings.csv", index=False)
        del ratings

        subprocess.check_call(f"rm {path}/{zip_filename}", shell=True)
        subprocess.check_call(f"rm -rf {path}/{FILENAME}", shell=True)
        subprocess.check_call(f"touch {marker_path}", shell=True)

        print("Finished downloading dataset...")

    except Exception as ex:
        subprocess.check_call(f"rm -rf {path}", shell=True)

        print("Failed to download dataset...: %s", ex)
