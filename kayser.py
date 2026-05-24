import pandas as pd
import os

# 1.setup
parquet_file = "studentss.parquet"
if not os.path.exists(parquet_file):
    df = pd.DataFrame(columns=['ID','name','age','grade'])
    df.to_parquet(parquet_file,engine="pyarrow",compression="snappy")

# 2.helper functions 
def load_data():
    return pd.read_parquet(parquet_file)

def save_data():
    return df.to_parquet(parquet_file,engine="pyarrow",compression="snappy")

