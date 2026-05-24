import pandas as pd

df = pd.read_csv("taxi_zone_lookup.csv")

print(df.head())
print("\nshape:",df.shape())
print("\nColumns:",df.columns.tolist())