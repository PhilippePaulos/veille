import os

from utils import spark_utils, fs


def count_partitions(iterator):
    yield len(list(iterator))


def count_partitions_idx(idx, iterator):
    yield 'index: {}, values: {}'.format(idx, list(iterator))


if __name__ == "__main__":
    sc = spark_utils.init_spark()
    rdd = spark_utils.read_text_file(sc, fs.get_resources_file("quote.txt"), min_partitions=3)
    print(rdd.mapPartitions(count_partitions).collect())
    print(rdd.mapPartitionsWithIndex(count_partitions_idx).collect())

