
if __name__ == '__main__':
    from pyspark.sql import SparkSession
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType

    def start_sparksession():
        return (
            SparkSession.builder.appName('Readfile').master('local[1]').getOrCreate()
        )


    spark = start_sparksession()

    # def schema_defining(n):  # 'n' is number of columns

    file = r'/home/antrikshhii17/pyspark/Data7602DescendingYearOrder.csv'

    sparkDF = spark.read.csv(file)
    # sparkDF.collect()
    sparkDF.coalesce(1).write.format('com.databricks.spark.avro').save(r'/home/antrikshhii17/pyspark/Newfile.avro')
    print('File written successfully')
