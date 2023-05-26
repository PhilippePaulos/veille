from pyspark import RDD
from pyspark.sql import SparkSession


def init_spark():
    return SparkSession.builder.getOrCreate()


def read_text_file(sc: SparkSession, path: str, min_partitions=None) -> RDD:
    return sc.sparkContext.textFile(path, min_partitions)


def read_csv_file(sc: SparkSession, path: str, header=True, **additional_options):
    return sc.read.options(header=header, **additional_options).csv(path)
