import pandas as pd


df = pd.read_csv("data/address_book.csv")
df_mean = df.groupby("Zipcode").mean()
print(df_mean)