from pyspark.sql import SparkSession
import base64

spark = SparkSession \
    .builder \
    .master("local") \
    .config("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .getOrCreate()

df = spark.read.format("bigquery").option("project", "bigquery-public-data").option("table", "samples.github_timeline").load()
