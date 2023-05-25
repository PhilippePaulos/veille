import importlib.resources

import numpy as np
import pandas as pd

from common.helpers import get_resources_file


def read_file_as_df(path: str, **options) -> pd.DataFrame:
    return pd.read_csv(str(path), **options)


def compute_stats(df: pd.DataFrame) -> dict:
    stats = ['mean', 'min', 'max', 'sum']
    aggs = {col: stats for col in ['salaire', 'age']}
    stats_df = df.agg(aggs).T
    stats_df = stats_df.reset_index().melt(id_vars='index', var_name='stat')
    stats_df['stat'] = stats_df['index'] + '_' + stats_df['stat']
    stats_df = stats_df.pivot_table(index=None, columns='stat', values='value', aggfunc='first')
    stats = stats_df.to_dict('records')[0]
    return stats


def grouping_stats() -> None:
    salaires_df = read_file_as_df(get_resources_file('salaries.csv'))
    departements_df = read_file_as_df(get_resources_file('departments.csv'))

    df = pd.merge(salaires_df, departements_df, left_on='dpt_id', right_on='id')
    df['salaire_sum'] = df.groupby('departement')['salaire'].transform(np.sum)


def clean_df(df: pd.DataFrame, stats: dict) -> pd.DataFrame:
    fills = {'salaire': 'mean', 'age': 'min'}
    for col, func in fills.items():
        df[col].fillna(stats[f'{col}_{func}'], inplace=True)
    return df


def query(df):
    filter = df['age'] > 30
    print(df.loc[filter])
    print(df.drop(df[filter].index, axis=0))


def cast(df: pd.DataFrame) -> pd.DataFrame:
    return df.astype({'age': 'Int64'})


if __name__ == "__main__":
    df = read_file_as_df(get_resources_file('bad.csv'))
    df = cast(df)
    print(df)
    stats = compute_stats(df)
    cleaned_df = clean_df(df, stats)
    query(cleaned_df)
    grouping_stats()
