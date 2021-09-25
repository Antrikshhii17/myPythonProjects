from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import *
from pyspark.sql import functions as F
import re

# This is our SparkSession to work on Spark dataframe
spark = SparkSession.builder.appName("Process text file").getOrCreate()

# This is our SparkContext to work on RDDs
conf = SparkConf().setAppName('Reading textfile').setMaster('local[*]')
sc = SparkContext(conf=conf).getOrCreate()

file = r'C:\Users\antriksh.chourasia\Documents\parsed3.txt'
with open(file) as file1:
    lines = file1.readlines()

# Slicing the list into smaller lists
chunks = [lines[i:i+3] for i in range(0, len(lines), 3)]
print(chunks, sep='\n')

savepath = '/home/antrikshhii17/learn_bash/properfile.txt'
with open(savepath, 'w') as nsave:
    for rowd in chunks:
        nsave.write(f'{rowd}\n')

# Reading the text file into RDD
rdd1 = sc.textFile(file)

# Removing the unwanted tabs from all the columns
rdd2 = rdd1.map(lambda x: x.replace('-', ''))
rdd2 = rdd2.map(lambda x: '|' + x if re.match('[0-9]', x) else x)
rdd3 = rdd2.map(lambda x: x.strip())
rdd4 = rdd3.map(lambda x: x if re.match('\t[1-9]', x) else x.replace('\t', ''))

# To remove Nulls or empty cells/rows
rdd3 = rdd3.filter(lambda x: x)

# Defining header
header = rdd4.take(3)
rdd5 = rdd4.filter(lambda x: x != header)

# Splitting the RDD so that it can be converted to comma separated dataframe
rdd6 = rdd5.map(lambda x: x.split('\t', x))
rdd6.coalesce(1).saveAsTextFile('newfile')

# Defining schema for createDataFrame()
Schema1 = StructType([
    StructField('SNo', IntegerType(), True),
    StructField('Name of the Organisation', StringType(), True),
    StructField('Website', StringType(), True)
])

# Defining schema for toDF()
schema2 = ['SNo', 'Organization', 'Website']

# Converting the RDD to dataframe using createDataFrame() along with defining the columns
newdf1 = spark.createDataFrame(rdd6, Schema1)
newdf1 = rdd1.map(lambda x: x.split(',')).toDF(schema2)

# Further cleaning
newdf2 = newdf1.withColumn('SNo', F.regexp_replace('SNo', '\[', ''))
newdf2 = newdf2.withColumn('Website', F.regexp_replace('Website', '\]', ''))

# Writing dataframe to csv file
newdf2.write.csv(path='/home/antrikshhii17/learn_bash/processed_data', header=True)

# Stopping the SparkContext
sc.stop()
