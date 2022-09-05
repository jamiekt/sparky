from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("sparky").getOrCreate()

df = spark.read.parquet("examples/src/main/resources/users.parquet")

df.show()