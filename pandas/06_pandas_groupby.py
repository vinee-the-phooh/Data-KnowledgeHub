#Pandas GroupBy Module
#Goal: Learn how to group data and calculate summary statistics

import pandas as pd

#Sample DataFrame
data = {
    "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT"],
    "Employee": ["Harsha", "Bob", "Maya", "David", "Eva", "Lila"],
    "Salary": [50000, 55000, 60000, 62000, 70000, 72000],
    "Bonus": [5000, 6000, 4000, 4500, 8000, 8500]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Group by Department
grouped = df.groupby("Department")
print("\nGrouped by Department (object):\n", grouped)

#Aggregate: mean salary per department
mean_salary = grouped["Salary"].mean()
print("\nMean Salary per Department:\n", mean_salary)

#Aggregate multiple columns
summary = grouped[["Salary", "Bonus"]].mean()
print("\nMean Salary and Bonus per Department:\n", summary)

#Use .agg() for custom aggregation
custom_agg = grouped.agg({
    "Salary": ["mean", "max"],
    "Bonus": ["sum", "min"]
})
print("\nCustom Aggregation:\n", custom_agg)

#Group and count
count_per_dept = grouped["Employee"].count()
print("\nEmployee Count per Department:\n", count_per_dept)

#Reset index (optional)
summary_reset = summary.reset_index()
print("\nSummary with Reset Index:\n", summary_reset)

#My Note:
    #groupby("col") : creates grouped object
    #Use .mean(), .sum(), .count(), etc. on grouped data
    #Use .agg() for multiple or custom aggregations
    #Reset index for clean output

    #df.groupby("col"): group rows by column
    #.mean(), .sum(), .count(): apply to groups
    #.agg({...}): custom aggregation
    #.reset_index():flatten grouped result