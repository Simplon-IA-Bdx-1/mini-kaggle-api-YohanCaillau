import pandas as pd
import csv

trainfull = pd.read_csv("C:/Users/utilisateur/Desktop/exo_louis_28-07-2020/trainfull.csv", encoding='utf-8')

df_train=trainfull.sample(frac=0.8,random_state=42)
df_test=trainfull.drop(df_train.index)

df_train.to_csv("C:/Users/utilisateur/Desktop/exo_louis_28-07-2020/train.csv", index=False)
df_test.to_csv("C:/Users/utilisateur/Desktop/exo_louis_28-07-2020/test2.csv", index=False)