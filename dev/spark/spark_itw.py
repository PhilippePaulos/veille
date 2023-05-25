from pyspark import RDD
from pyspark.sql import SparkSession, functions as F, Window
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, DoubleType

from common.helpers import get_resources_file


def init_spark():
    return SparkSession.builder.getOrCreate()


def read_text_file(sc: SparkSession, path: str) -> RDD:
    return sc.sparkContext.textFile(path)


def read_csv_file(sc: SparkSession, path: str, header=True, **additional_options):
    return sc.read.options(header=header, **additional_options).csv(path)


def word_count(file_rdd: RDD) -> None:
    word_counts = (
        file_rdd.flatMap(lambda line: line.split(' '))
        .map(lambda word: (word, 1))
        .reduceByKey(lambda a, b: a + b)
    )
    for word, count in word_counts.collect():
        print(f'{word}: {count}')


def people_exercice(sc) -> None:

    people_df = read_csv_file(sc, get_resources_file('people.csv'))

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


def display_dataframes(*dfs) -> None:
    for df in dfs:
        df.show()


def sql_operations() -> None:
    salaries_df = read_csv_file(sc, get_resources_file('salaries.csv'))

    high_salaries_df = salaries_df.where(F.col('salaire') > 4500)
    avg_df = salaries_df.agg(F.avg(F.col('salaire')))
    max_salary_df = salaries_df.agg(F.max(F.col('salaire')))

    rank_df = salaries_df.withColumn('salary_rank',
                                     F.rank().over(Window.partitionBy().orderBy(F.desc('salaire'))))

    display_dataframes(high_salaries_df, avg_df, max_salary_df, rank_df)


def enrichment() -> None:
    salaries_df = read_csv_file(sc, get_resources_file('salaries.csv'))
    departments_df = read_csv_file(sc, get_resources_file('departments.csv'))
    enrichement_df = salaries_df.join(departments_df, salaries_df.dpt_id == departments_df.id, 'inner')

    agg_df = enrichement_df.groupBy('departement').agg(F.avg('salaire').alias('avg_salaire'),
                                              F.max('salaire').alias('max_salaire'),
                                              F.min('salaire').alias('min_salaire'))

    avg_salary = int(salaries_df.select(F.avg('salaire')).collect()[0][0])
    filled_df = enrichement_df.withColumn('salaire', F.when(F.col('salaire').isNull(), F.lit(avg_salary))
                                          .otherwise(F.col('salaire')))
    display_dataframes(enrichement_df, agg_df, filled_df)


def handle_bad_data() -> None:
    bad_data_df = read_csv_file(sc, get_resources_file('bad.csv'), inferSchema=True)
    schema = bad_data_df.schema
    avg_dict = {col: 'mean' for col in bad_data_df.columns if schema[col].dataType in [IntegerType(), DoubleType()]}
    mode_dict = {col: 'mode' for col in bad_data_df.columns if schema[col].dataType in [IntegerType(), DoubleType()]}
    avg_df = bad_data_df.agg(avg_dict)
    mode_df = bad_data_df.agg(mode_dict)

    for col in avg_dict.keys():
        bad_data_df = bad_data_df.na.fill(avg_df.first()[f'avg({col})'], subset=[col])

    for col in mode_dict.keys():
        bad_data_df = bad_data_df.na.fill(mode_df.first()[f'mode({col})'], subset=[col])

    display_dataframes(bad_data_df)


if __name__ == "__main__":
    sc = init_spark()
    text_file = read_text_file(sc, get_resources_file('quote.txt'))

    word_count(text_file)
    people_exercice(sc)
    sql_operations()
    enrichment()
    handle_bad_data()
