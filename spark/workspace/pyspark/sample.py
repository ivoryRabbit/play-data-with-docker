import sys

from pyspark.sql import SparkSession
from pyspark.context import SparkContext


if __name__ == "__main__":
    spark = SparkSession.builder.appName("local").getOrCreate()

    spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")
    spark.conf.set("spark.sql.session.timeZone", "Asia/Seoul")
