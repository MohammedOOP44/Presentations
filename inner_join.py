import pandas as pd

df_employees = pd.DataFrame({
    "Employee_ID" : [1,2,3,4],
    "names" : ['Alice', 'Bob', 'Charlie', 'David'],
    "Dept_ID" : [10,20,10,30]
})

df_departments = pd.DataFrame({
    "Dept_ID" : [10,20,30],
    "Dept_name" : ['HR', 'IT', 'Marketing']
})

df_inner = pd.merge(df_employees,df_departments,on="Dept_ID",how='inner')
print(df_inner)