from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("sparky").getOrCreate()

df = spark.read.json("examples/src/main/resources/people.json")

df.createOrReplaceTempView("people")

# sqlDf = spark.sql("select * from people")
# sqlDf.show()

# print(spark.catalog.listTables())