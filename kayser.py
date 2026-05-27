import pandas as pd 
import os 

# 1. setup 
parquet_file = "students1.parquet"
if not os.path.exists(parquet_file):
    df = pd.DataFrame(columns=["ID","name","age","grade"])
    df.to_parquet(parquet_file,engine="pyarrow",compression="snappy")

# 2. Helper functions
def load_data():
    return pd.read_parquet(parquet_file)

def save_data(df):
    return df.to_parquet(parquet_file,engine="pyarrow",compression="snappy")

# 3.CRUD

def add_student(name,age,grade):
    df = load_data()
    new_id = (df["ID"].max()+1) if not df.empty else 1
    new_row = pd.DataFrame([[new_id,name,age,grade]],columns=df.columns)
    df = pd.concat([df,new_row],ignore_index=True)
    save_data(df)
    print("student added successfully")
    print("-" * 20)

def view_students():
    df = load_data()
    print("\nSTUDENT LIST:")
    print(df)

def update_student(student_id,new_grade):
    df = load_data()
    df.loc[df["ID"] == student_id , "grade"] = new_grade
    save_data(df)

def delete_student(student_id):
    df = load_data()
    df = df[df["ID"] != student_id]
    save_data(df)

def search_by_name(name):
    df = load_data()
    results = df[df["name"].str.contains(name,case=False,na=False)]
    print(f"search student for name {name}:")
    print(results)

def search_by_grade(grade):
    df = load_data()
    results = df[df["grade"]==grade]
    print(f"student with grade {grade}")
    print(results)

def import_student_from_csv(csv_file):
    df = load_data()
    new_df = pd.read_csv(csv_file)
    new_df = new_df.dropna(subset=['name','age','grade'])
    new_df["ID"] = range(df['ID'].max() + 1 if not df.empty else 1,
                         df['ID'].max() + 1 + len(new_df))
    df = pd.concat([df,new_df],ignore_index=True)
    save_data(df)
    print("student imported successfully from csv")

def export_student_to_csv(file_name="student_export.csv"):
    df = load_data()
    df.to_csv(file_name,index=False)
    print(f"student exported successfully to {file_name}")   

# 5.menu
def menu():
    while True:
        print("--- student managment system (parquet) ---")
        print("1.add student") 
        print("2.view students") 
        print("3.update students grade") 
        print("4.delete student")
        print("5.search by name") 
        print("6.search by grade") 
        print("7.import student from csv") 
        print("8.export student to csv")
        print("9.Exit")

        choice = int(input('Enter choice: '))

        if choice == 1:
            name = input("Enter the student name: ")
            age = input("Enter the student age: ")
            grade = input("Enter the student grade: ")
            add_student(name,age,grade)

        elif choice == 2:
            view_students()

        elif choice == 3:
            s_id = int(input("Enter the ID of the student: "))
            new_grade = int(input("Enter the new grade"))
            update_student(s_id,new_grade) 

        elif choice == 4:
            st_id = int(input("Enter the ID of the student you wanna delete rn: "))
            delete_student(st_id)

        elif choice == 5:
            s_name = input("Enter the student name: ")
            search_by_name(s_name)

        elif choice == 6:
            s_grade = input("Enter the student grade: ")
            search_by_grade(s_grade)

        elif choice == 7:
            csv_file = input("Enter the csv file name to import: ")
            import_student_from_csv(csv_file)

        elif choice == 8:
            file_name = input("Enter file name to export: ")
            if file_name == "":
                file_name = "student_export.csv"
            export_student_to_csv(file_name)

        elif choice == 9:
            print("Exiting...")
            break 

        else:
            print("invalid choice, try later bro")

menu()

