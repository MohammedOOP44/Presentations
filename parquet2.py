import os
import pandas as pd

# 1.setup
Parquet_File = "studentsss.parquet"
if not os.path.exists(Parquet_File):
    df = pd.DataFrame(columns=['ID','Name','Age','Grade'])
    df.to_parquet(Parquet_File,engine="pyarrow",compression="snappy")

# 2.helper functions
def load_data():
    return pd.read_parquet(Parquet_File)

def save_data(df):
    return df.to_parquet(Parquet_File,engine="pyarrow",compression="snappy")

# 3. CRUD
def add_student(self,name,age,grade):
    df = load_data()
    new_id = (df['ID'].max()) if not df.empty else 1 
    new_row = pd.DataFrame([new_id,name,age,grade],columns=df.columns)
    df = pd.concat([df,new_row],ignore_index=True)
    save_data(df)
    print("student added successfully")
    
def view_students():
    df = load_data()
    print("\nSTUDENT LIST:")
    print(df)

def update_student(st_id,new_grade):
    df = load_data()
    df.loc[df['ID'] == st_id,'Grade'] = new_grade
    save_data(df)

def delete_student(st_id):
    df = load_data()
    df = df[df['ID'] != st_id]
    save_data(df)

def search_by_name(name):
    df = load_data()
    results = df[df['Name'].str.contains(name,case=False,na=False)]
    print(f"search result for name {name}")
    print(results)

def search_by_grade(grade):
    df = load_data()
    results = df[df['Grade']==grade]
    print(f"student with grade {grade}")

def import_student_from_csv(csv_file):
    df = load_data()
    new_df = pd.read_csv(csv_file)
    new_df = new_df.dropna(subset=['Name','Age','Grade'])
    new_df['ID'] = range(df['ID'].max() + 1 if not df.empty else 1,
                         df['ID'].max() + 1 + len(new_df))
    df = pd.concat([df,new_df], ignore_index=True)
    save_data(df)

def export_student_to_csv(file_name="student_export.csv"):
    df = load_data()
    df.to_csv(file_name,index=False)
    print(f"student exported successfully to {file_name}")

    