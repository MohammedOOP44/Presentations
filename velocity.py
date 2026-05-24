import pandas as pd

# create_data
data = {
    "fare_amount":[10,20,30,40,50]*100
}
df = pd.DataFrame(data)
df.to_csv("taxii.csv")
# volume 
print("row,cols",df.shape)

# velocity
chunks = pd.read_csv("taxii.csv",chunksize=50)
for i,chunk in enumerate(chunks):
    print(f"chunk {i} Average fare: {chunk['fare_amount'].mean()}")

df_csv = pd.read_csv("taxii.csv")
df_json = pd.read_json("taxii.json")
