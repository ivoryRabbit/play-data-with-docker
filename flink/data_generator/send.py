import requests

import pandas as pd

rating_df = pd.read_csv("/tmp/flink/dataset/ratings.csv").sort_values("timestamp")

i = 0
rate_limit = 10

url = "http://localhost:8082/review/rating"
headers = {"accept": "application/json"}


class Rating(BaseModel):
    user_id: int = Field(..., serialization_alias="userId")
    movie_id: int = Field(..., serialization_alias="movieId")
    rating: float = Field(..., serialization_alias="rating")
    timestamp: int = Field(..., serialization_alias="timestamp")


for user_id, movie_id, rating, timestamp in rating_df.itertuples(index=False):
    rating = Rating(
        user_id=int(user_id),
        movie_id=int(movie_id),
        rating=float(rating),
        timestamp=int(timestamp),
    )

    data = rating.model_dump_json(by_alias=True)
    response = requests.post(url=url, data=data, headers=headers)

    print(response.status_code)

    i += 1
    if i == rate_limit:
        break
