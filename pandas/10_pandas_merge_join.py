#Pandas Merge & Join Module
#Goal: Combine datasets using merge(), join(), and concat()

import pandas as pd

#Sample DataFrames
df_employees = pd.DataFrame({
    "EmpID": [101, 102, 103],
    "Name": ["Harsha", "Vinee", "Amara"],
    "DeptID": [1, 2, 1]
})

df_departments = pd.DataFrame({
    "DeptID": [1, 2],
    "Department": ["Sales", "HR"]
})

print("Employees:\n", df_employees)
print("\nDepartments:\n", df_departments)

#Merge on DeptID (inner join by default)
merged = pd.merge(df_employees, df_departments, on="DeptID")
print("\nMerged DataFrame:\n", merged)

#Left join (keep all employees)
left_join = pd.merge(df_employees, df_departments, on="DeptID", how="left")
print("\nLeft Join:\n", left_join)

#Outer join (keep all rows from both)
outer_join = pd.merge(df_employees, df_departments, on="DeptID", how="outer")
print("\nOuter Join:\n", outer_join)

#Join using index
df_dept_indexed = df_departments.set_index("DeptID")
joined = df_employees.join(df_dept_indexed, on="DeptID")
print("\nJoin using index:\n", joined)

#Concatenate vertically (stack rows)
df_new = pd.DataFrame({
    "EmpID": [104],
    "Name": ["David"],
    "DeptID": [2]
})
concat_df = pd.concat([df_employees, df_new], ignore_index=True)
print("\nConcatenated DataFrame:\n", concat_df)

#My Note:
    #merge() : combine on column(s)
    #join() : combine using index
    #concat() : stack rows or columns
    #how="left"/"right"/"outer"/"inner" : control join type

    #pd.merge(df1, df2, on="col") : merge on column
    #df1.join(df2, on="col") : join using index
    #pd.concat([df1, df2]) : stack vertically or horizontally
    #how="left"/"right"/"outer"/"inner" : join type