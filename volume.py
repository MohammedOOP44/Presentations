import pandas as pd
# csv
data_csv = {
    "fare": [10, 20], 
    "driver": ["Ali", "Sara"]
}
df_from_csv = pd.DataFrame(data_csv)
df_from_csv.to_csv("taxiii.csv",index=False)

# JSON
data_json = [
    {"driver": "Ali", "info": {"rating": 5, "car": "Tesla"}},
    {"driver": "Sara", "info": {"rating": 4, "car": "Toyota"}}
]

df_from_json = pd.DataFrame(data_json)
df_from_json.to_json("taxiii.json")

import json
with open("taxiii.json","w") as f:
    json.dump(data_json, f)

# reading them 
read_csv = pd.read_csv("taxiii.csv")
read_json = pd.read_json("taxiii.json")

print("CSV COLUMNS",read_csv.columns.tolist())
print("JSON COLUMNS",read_json.columns.tolist())




