# volume 
import pandas as pd


data = {
    "fare_amount" : {10,20,30,40,50} * 100
}
df = pd.DataFrame(data)
df.to_csv("taxi.csv",index=False)

df = pd.read_csv("taxi.csv")
print("rows,col",df.shape)
print(df)

# velocity
chunks = df.read_csv("taxi",chunksize=100)
for i , chunk in enumerate(chunks):
    print(f"chunk {i} average fare:",chunk["fare_amount"].mean())
