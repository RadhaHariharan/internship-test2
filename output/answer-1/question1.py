import pandas as pd
table = pd.read_csv("main.csv")
table.head()
table.groupby('product_description')['price'].mean()
table["price_new"] = table['price'].fillna(
   table.groupby('product_description')['price'].transform("mean")
)
table[table["price"].isna()].head()
