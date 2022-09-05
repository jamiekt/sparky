from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("read from parquet").getOrCreate()

df = spark.read.parquet("sampledata/parquet")

df.show()