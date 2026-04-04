import pandas as pd
import matplotlib.pyplot as plt
import pyodbc 
import warnings 
warnings.filterwarnings('ignore',category=UserWarning)
print("Modules loaded! We are ready to rock.")

# ===================================
# Step 1: Database Connection Setup
# ===================================
# We gotta define where the database is crashing at on your PC (Update this path!).
# The 'r' before the string means "Raw string". It stops backslashes (\) from messing things up.
DB_PATH = r"C:\Users\AL-AJIAL\Downloads\AI training lifecycle and dataset management system2.accdb"
# Wiring up the connection string (Telling Python exactly what driver and path to use).
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=' + DB_PATH + ';'
)
print(f"🔗 Ready to hook up with the database at: {DB_PATH}")

# ===================================
# Step 2: Connecting and Fetching Data
# ===================================
print("⏳ Attempting to open the vault...")

try:
    # بنفتح الاتصال الفعلي بقاعدة البيانات
    # Opening the actual pipeline to the database.
    conn = pyodbc.connect(conn_str)
    # بنسحب الجداول باستخدام أوامر SQL وبنخزنها في DataFrames
    # Ripping the tables out using SQL queries and dropping them into DataFrames.
    models   = pd.read_sql('SELECT * FROM AI_Models',conn)
    datasets = pd.read_sql('SELECT * FROM Datasets',conn)
    logs     = pd.read_sql('SELECT * FROM Training_Logs',conn)

    # بنقفل الاتصال عشان منستهلكش رامات الجهاز على الفاضي ومفيش ملفات تبوظ
    # Shutting down the connection so we don't hog system memory or corrupt files.
    conn.close()

except Exception as e:
    print(f"❌ Connection failed, boss! Error: {e}")
    exit()

# Printing the row counts just to make sure we grabbed everything smoothly.
print(f"   • AI_Models    : {len(models)} records")
print(f"   • Datasets     : {len(datasets)} records")
print(f"   • Training_Logs: {len(logs)} records")

# ===================================
# Step 3 & 4: Merging and Cleaning Data
# ===================================
print("\n🧩 Putting the puzzle pieces together...")

full = logs.merge(models , on='Model_ID')
full = full.merge(datasets , on='Dataset_ID')
# Flipping the accuracy column into raw numbers, and sweeping any junk data under the rug as NaN (coerce).

full['Accuracy_score'] = pd.to_numeric(full['Accuracy_score'], errors='coerce')
full['Training_Duration_Hrs'] = pd.to_numeric(full['Training_Duration_Hrs'], errors='coerce')
full['Execution_Date'] = pd.to_datetime(full['Execution_Date'], errors='coerce')
print("\n--- First 5 rows of our Mega-Table ---")
print(full.head())

