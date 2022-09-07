# https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#quick-example

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
from pyspark.sql import DataFrame

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount").getOrCreate()

lines = spark \
    .readStream \
    .format("socket") \
    .option("host","localhost") \
    .option("port", 9999) \
    .load()

words: DataFrame = lines.select(
    explode(
        split(lines.value, " ")
    ).alias("word")
)

wordCounts: DataFrame = words.groupBy("word").count()

query = wordCounts \
        .writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()

query.awaitTermination()