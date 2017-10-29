import tkinter
from math import log2
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", palette="muted", color_codes=True)

def log(series: pd.Series) :
    # print(series)
    transformed = [0 for _ in range(series.size)]
    for i, el in enumerate(series):
        # print(el)
        transformed[i] = log2(el) if el != 0 else log2(1)
    return transformed

def replace(values, subst_dict):
    return [subst_dict[value] for value in values]


def normalize(df: pd.DataFrame):
    ranks = df.rank(axis=0, method='min') # type: pd.DataFrame
    sorted_df = pd.DataFrame({key: sorted(value) for key, value in df.iteritems()}) # type: pd.DataFrame
    means = sorted_df.mean(axis=1)
    mean_ranks = means.rank(axis=0, method='min')
    subst_dict = {key_: value_ for key_, value_ in zip(mean_ranks, means)}
    return pd.DataFrame({key: replace(value, subst_dict) for key, value in ranks.iteritems()})


def normalize_simple(df: pd.DataFrame):
    ranks = df.rank(axis=0, method='min') # type: pd.DataFrame
    sorted_df = pd.DataFrame()
    for key, value in df.iteritems():
        sorted_df[key] =  sorted(value)
    means = sorted_df.mean(axis=1)
    mean_ranks = means.rank(axis=0, method='min')
    subst_dict = {key_: value_ for key_, value_ in zip(mean_ranks, means)}
    normalized_df = pd.DataFrame()
    for key, value in ranks.iteritems():
        normalized_df[key] = replace(value, subst_dict)
    return normalized_df

# data_df = pd.read_csv('GSE89225_Illumina_counts.csv')
data_df = pd.read_csv('edata.csv')
# mart_df = pd.read_csv('human_mart.txt')
print(data_df)

f, axes = plt.subplots(1, 2, figsize=(7, 7), sharex=True)
sns.despine(left=True)


# Get rid of 0 data
data_df = data_df[data_df.mean(axis=1) > 3]


norm_data = normalize_simple(data_df[['NA06985', 'NA06986', 'NA07000']])
# print(norm_data['NA06985'])
# print(data_df['NA06985'])
#
sns.distplot(log(norm_data['NA06985']), hist=False, color="g", kde_kws={"shade": True}, ax=axes[0])
sns.distplot(log(data_df['NA06985']), hist=False, color="b", kde_kws={"shade": True}, ax=axes[1])
sns.distplot(log(data_df['NA06986']), hist=False, color="r", kde_kws={"shade": True}, ax=axes[1])
sns.distplot(log(norm_data['NA06986']), hist=False, color="purple", kde_kws={"shade": True}, ax=axes[0])
sns.distplot(log(norm_data['NA07000']), hist=False, color="r", kde_kws={"shade": True}, ax=axes[0])
sns.distplot(log(data_df['NA07000']), hist=False, color="r", kde_kws={"shade": True}, ax=axes[1])
# sns.distplot(norm_data, hist=False, color="g", kde_kws={"shade": True}, ax=axes[0])

#
# plt.tight_layout()



#