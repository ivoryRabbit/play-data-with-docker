import json

import requests
import pandas as pd

from dataset import load_data


if __name__ == "__main__":
    load_data("/tmp/flink/dataset")
    rating_df = pd.read_csv("/tmp/flink/dataset/ratings.csv").sort_values("timestamp")

    url = "http://localhost:8082/review/rating"
    headers = {"accept": "application/json"}

    for user_id, movie_id, rating, timestamp in rating_df.itertuples(index=False):
        payload = dict(
            user_id=int(user_id),
            movie_id=int(movie_id),
            rating=float(rating),
            timestamp=int(timestamp),
        )

        response = requests.post(url=url, data=json.dumps(payload), headers=headers)
        print(response.status_code)
