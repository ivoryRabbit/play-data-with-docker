import logging
import subprocess
import zipfile
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def download_data(dir: str):
    logger.info("Start loading MovieLens dataset...")

    FILENAME = "ml-1m"
    MARKER = "_SUCCESS"

    local_path = Path(dir).resolve()
    local_path.mkdir(parents=True, exist_ok=True)

    marker_path = str(local_path.joinpath(MARKER))

    if Path(marker_path).is_file() is True:
        logger.info("MovieLens dataset already exists...")
        return

    try:
        zip_filename = f"{FILENAME}.zip"
        download_url = f"https://files.grouplens.org/datasets/movielens/{zip_filename}"
        subprocess.check_call(f"curl -o {dir}/{zip_filename} {download_url}", shell=True)

        file_zip = zipfile.ZipFile(f"{dir}/{zip_filename}")
        file_zip.extractall(local_path)

        users = pd.read_csv(
            f"{dir}/{FILENAME}/users.dat",
            delimiter="::",
            names=["id", "gender", "age", "occupation", "zip_code"],
            engine="python",
            encoding="ISO-8859-1",
        )

        users.to_csv(f"{dir}/users.csv", index=False)
        del users

        movies = pd.read_csv(
            f"{dir}/{FILENAME}/movies.dat",
            delimiter="::",
            names=["id", "title", "genres"],
            engine="python",
            encoding="ISO-8859-1",
        )
        movies[["title", "year"]] = movies["title"].str.extract(
            r"(?P<title>.*) [(](?P<year>\d+)[)]$"
        )

        movies.to_csv(f"{dir}/movies.csv", index=False)
        del movies

        subprocess.check_call(f"rm {dir}/{zip_filename}", shell=True)
        subprocess.check_call(f"rm -rf {dir}/{FILENAME}", shell=True)
        subprocess.check_call(f"touch {marker_path}", shell=True)

        logger.info("Finished downloading dataset...")

    except Exception as ex:
        subprocess.check_call(f"rm -rf {dir}", shell=True)

        logger.info("Failed to download dataset...: %s", ex)


if __name__ == "__main__":
    download_data(dir="dbt_test/seeds")
