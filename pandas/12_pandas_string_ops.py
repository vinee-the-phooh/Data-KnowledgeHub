#Pandas String Operations Module
#Goal: Clean and manipulate text data using .str methods

import pandas as pd

# 🔹 Sample DataFrame with text
data = {
    "Name": ["Harsha Dush", "Bob Jones", "Rani Maya", "Gaya Wijay"],
    "Email": ["Dush@example.com", "bob@work.org", "rani@edu.net", "gaya@company.com"]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Convert to lowercase
df["Email_lower"] = df["Email"].str.lower()
print("\nLowercase Emails:\n", df)

#Extract domain from email
df["Domain"] = df["Email"].str.split("@").str[1]
print("\nExtracted Domain:\n", df)

#Check if name contains "Smith"
df["Has_Smith"] = df["Name"].str.contains("Harsha")
print("\nContains 'Harsha':\n", df)

#Replace domain suffix
df["Email_updated"] = df["Email"].str.replace(".com", ".org", regex=False)
print("\nUpdated Email Domain:\n", df)

#String length
df["Name_length"] = df["Name"].str.len()
print("\nName Length:\n", df)

# 🔸 Extract first name
df["FirstName"] = df["Name"].str.split().str[0]
print("\nFirst Name:\n", df)

#My Note:
    #Use .str to access string methods
    #.str.lower(), .str.contains(), .str.replace(), .str.split()
    #Great for cleaning, extracting, and transforming text

    #.str.lower() : lowercase
    #.str.contains("text") : check match
    #.str.replace("old", "new") : replace text
    #.str.split("sep").str[n] : split and extract part
    #.str.len() : string length