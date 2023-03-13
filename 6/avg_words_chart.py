#BASED ON NUMBER OF TWEETS FOR AVERAGE WORDS HS AND ABUSIVE CHART

import pandas as pd

from matplotlib import pyplot as plt

import seaborn as sns

df = pd.read_csv('data.csv', encoding='latin-1')

df['avg_char'] = df.Tweet.apply(len)

df["avg_words"] = df["Tweet"].apply(lambda n: len(n.split()))

df_new = df.drop_duplicates()

stats_df_new = df_new.drop(['Tweet'], axis=1)

melted_df_new = pd.melt(stats_df_new, 
                   id_vars=["avg_char", "avg_words"],
                    var_name="Stat")

id=melted_df_new[melted_df_new['value']==0].index

melted_df_new2=melted_df_new.drop(id)

type_colors = ['#78C850', 
                    '#F08030',  
                    '#6890F0',  
                    '#A8B820', 
                    '#A8A878',  
                    '#A040A0',  
                    '#F8D030',  
                    '#E0C068',  
                    '#EE99AC',  
                    '#C03028',  
                    '#F85888',  
                    '#B8A038', 
                    '#705898',  
                    '#98D8D8',  
                    '#7038F8',  
                   ]

plt.figure(figsize=(9,6))

sns.barplot(x='Stat', y='avg_words', data=melted_df_new2, palette=type_colors)

plt.xticks(rotation=-30)

plt.show()