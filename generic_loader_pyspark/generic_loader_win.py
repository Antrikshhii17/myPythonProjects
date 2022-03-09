from os import listdir
from pyspark.sql import SparkSession

filepath = "C:/Users/lenovo/PycharmProjects/generic_loader_pyspark/Load_files/"

files2 = listdir(filepath)
files = str(listdir(filepath))
fullPath = filepath + files[2:-2]
# print(fullPath)
spark = SparkSession.builder.appName('File_loader').getOrCreate()


def FileLoader(files2, files):
    if len(files2) > 1:
        print('There are more than 1 files. Please keep only one file in the directory.')
    elif files.endswith(".csv']"):
        print('This is a CSV file. Reading...')
        sparkDF = spark.read.csv(fullPath)
    elif files2.endswith(".xlsx']"):
        print('Excel file incoming')
        sparkDF = spark.read.table(fullPath)
    elif files.endswith(".txt']"):
        print('This is a text file. Reading...')
        sparkDF = spark.read.text(fullPath)
    elif files.endswith(".json']"):
        print('Here we have a json file. Reading...')
        sparkDF = spark.read.json(fullPath)
    elif files.endswith(".parquet']"):
        print('We have a parquet file. Reading...')
        sparkDF = spark.read.parquet(fullPath)
    else:
        print('Only .csv, .xlsx, .txt, .json and .parquet files are handled currently.')
    return sparkDF.show(10)


if __name__ == '__main__':
    FileLoader(files2, files)
