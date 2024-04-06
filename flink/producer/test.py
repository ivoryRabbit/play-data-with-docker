import json
import requests

import pandas as pd

rating_df = pd.read_csv("/tmp/flink/dataset/ratings.csv").sort_values("timestamp")

i = 0
rate_limit = 10

url = "http://localhost:8000/review/rating"


for user_id, movie_id, rating, timestamp in rating_df.itertuples(index=False):
    data = {
        "user_id": int(user_id),
        "movie_id": int(movie_id),
        "rating": float(rating),
        "timestamp": int(timestamp),
    }

    response = requests.post(
        url=url,
        data=json.dumps(data),
        headers={"accept": "application/json"},
    )

    print(response.status_code)

    i += 1
    if i == rate_limit:
        break
