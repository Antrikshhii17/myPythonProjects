# Importing our libraries
from pyspark.sql import SparkSession
from pyspark.sql import functions as fn

# Creating SparkSession
ss = SparkSession.builder.appName('loadCSV').getOrCreate()

# Reading the CSV file into spark dataframe. Without header argument, spark will assign column headers as c0,c1 etc.
sparkDF = ss.read.csv('rangel.csv', header=True)

# Total row count of the spark dataframe
sparkDF.count()
sparkDF.show(20, False)  # Viewing only top 20 rows

# Printing schema of the spark dataframe
sparkDF.printSchema()

# Rounding up the values to 2 places of decimal
df1 = sparkDF.withColumn('value', fn.round(sparkDF['value'], 2))
sparkDF = df1
sparkDF.show()

# Count NULLs and NaNs in each column in the dataframe
df2 = sparkDF.select([fn.count(fn.when(fn.isnan(i) |
                                       fn.col(i).isNull(), i)).alias(i)
                      for i in sparkDF.columns])
df2.show()

# Now I will drop all the rows that contains Null in value column
sparkDF.dropna(subset=['value'])
sparkDF.show(20, False)
print('Total rowcount after removing Nulls: ', sparkDF.count())

# def mqy(value):              # First creating a python function
#     if 'Month' in value:
#         return list('M')
#     elif 'Year' in value:
#         return list('Y')
#     else:
#         return list('Q')
# # Converting python function to pyspark UDF
# udf_mqy = fn.udf(lambda v: mqy(v))

# Now creating new column called Absolute_Period in sparkDF
condition1 = fn.col('Desc').like('%Month%')
condition2 = fn.col('Desc').like('%Quarter%')

sparkDF = sparkDF.withColumn('Absolute_Period',
                             fn.concat(fn.year('Date'),
                                       fn.when(condition1, 'M')
                                       .when(condition2, 'Q')
                                       .otherwise('Y'),
                                       fn.when(condition1, fn.format_string('%02d', fn.month('Date')))
                                       .when(condition2, fn.format_string('%02d', fn.quarter('Date')))
                                       .otherwise('')))
sparkDF.show(20, False)
