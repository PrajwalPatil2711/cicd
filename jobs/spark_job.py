from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("ExampleJob").getOrCreate()
    data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
    df = spark.createDataFrame(data, ["Name", "Age"])
    df.show()



if __name__ == "__main__":
    main()
