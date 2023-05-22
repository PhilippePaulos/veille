from pathlib import Path

from pyspark import RDD
from pyspark.sql import SparkSession, functions as F, Window
from pyspark.sql.functions import udf


def init_spark():
    return SparkSession.builder.getOrCreate()


def read_text_file(sc: SparkSession, path: Path) -> RDD:
    return sc.sparkContext.textFile(str(path))


def read_csv_file(sc: SparkSession, path: Path, header=False):
    return sc.read.options(header=header).csv(str(path))


def word_count(file_rdd: RDD) -> None:
    word_counts = (
        file_rdd.flatMap(lambda line: line.split(' '))
        .map(lambda word: (word, 1))
        .reduceByKey(lambda a, b: a + b)
    )
    for word, count in word_counts.collect():
        print(f'{word}: {count}')


def people_exercice(sc):

    people_df = read_csv_file(sc, Path('resources/people.csv'), header=True)

    # V1
    ages_groups_df = people_df.withColumn(
        "GroupeAge1",
        F.when(F.col("Age") <= 30, "0-30")
        .when((F.col("Age") > 30) & (F.col("Age") <= 45), "31-45")
        .otherwise("46+"),
    )

    @udf
    def compute_age_group(age):
        if int(age) <= 30:
            return '0-30'
        elif 30 < int(age) <= 45:
            return '31-45'
        else:
            return '46+'
    #V2
    ages_groups_df = ages_groups_df.withColumn('GroupeAge2', compute_age_group(ages_groups_df['Age']))
    ages_groups_df.show()


def display_dataframes(*dfs):
    for df in dfs:
        df.show()


def sql_operations():
    salaries_df = read_csv_file(sc, Path('resources/salaries.csv'), header=True)

    high_salaries_df = salaries_df.where(F.col('salaire') > 4500)
    avg_df = salaries_df.agg(F.avg(F.col('salaire')))
    max_salary_df = salaries_df.agg(F.max(F.col('salaire')))

    rank_df = salaries_df.withColumn('salary_rank',
                                     F.rank().over(Window.partitionBy().orderBy(F.desc('salaire'))))

    display_dataframes(high_salaries_df, avg_df, max_salary_df, rank_df)


if __name__ == "__main__":
    sc = init_spark()
    text_file = read_text_file(sc, Path('resources/quote.txt'))

    word_count(text_file)
    people_exercice(sc)
    sql_operations()

