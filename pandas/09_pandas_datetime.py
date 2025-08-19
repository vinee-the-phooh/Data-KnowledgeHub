#Pandas DateTime Module
#Goal: Work with date/time data using pd.to_datetime()

import pandas as pd

#Sample DataFrame with date strings
data = {
    "Event": ["Login", "Logout", "Login", "Logout"],
    "Timestamp": ["2025-08-01 08:30", "2025-08-01 17:45",
                  "2025-08-02 09:00", "2025-08-02 18:00"]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Convert string to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
print("\nConverted to datetime:\n", df)

#Extract date parts
df["Date"] = df["Timestamp"].dt.date
df["Hour"] = df["Timestamp"].dt.hour
df["Weekday"] = df["Timestamp"].dt.day_name()
print("\nExtracted parts:\n", df)

#Filter by date range
mask = (df["Timestamp"] >= "2025-08-01") & (df["Timestamp"] < "2025-08-02")
filtered = df[mask]
print("\nEvents on 2025-08-01:\n", filtered)

#Sort by datetime
df_sorted = df.sort_values("Timestamp")
print("\nSorted by time:\n", df_sorted)

#Calculate time difference
df["TimeDiff"] = df["Timestamp"].diff()
print("\nTime difference between events:\n", df)

#My Note:
    #Use pd.to_datetime() to convert strings
    #Use .dt accessor to extract parts (year, month, day, hour)
    #Filter using datetime logic
    #Use .diff() for time gaps

    #pd.to_datetime() : convert string to datetime
    #.dt.year, .dt.month, .dt.day : extract parts
    #.dt.day_name() : get weekday name
    #df["col"].diff() : time difference between rows