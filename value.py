import pandas as pd 

# 1. Create data with some 'Variety' and 'Volume
data = {
    'fare_amount': [15.0, 20.0, 10.0, 50.0, 30.0],
    'trip_distance': [3.0, 5.0, 2.0, 10.0, 4.0],
    'payment_type': ['Card', 'Cash', 'Card', 'Card', 'Cash']
}
df = pd.DataFrame(data)

# 2. Extract VALUE
df['fare_per_mile'] = df['fare_amount'] / df['trip_distance']

# Group by payment type to see which customers are more 'Valuable'
avg_fare = df.groupby('payment_type')['fare_per_mile'].mean()

print("--- Data with New Value Metric ---")
print(df)

print("\n--- The Insight (Value) ---")
print(avg_fare)


