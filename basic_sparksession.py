from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
        .appName("sparky").getOrCreate()

df = spark.read.json("venv/lib/python3.8/site-packages/pyspark/examples/src/main/resources/people.json")

df.show()


