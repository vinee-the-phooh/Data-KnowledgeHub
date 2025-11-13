import pandas as pd
import numpy as np
import random

np.random.seed(42)

rows = 120

data = {
    "TV_Spend": np.random.normal(20000, 5000, rows).round(2),
    "Radio_Spend": np.random.normal(10000, 3000, rows).round(2),
    "SocialMedia_Spend": np.random.normal(8000, 2500, rows).round(2),
    "Influencer_Score": np.random.randint(1, 11, rows),
    "Product_Category": np.random.choice(["A", "B", "C"], rows),
    "Region": np.random.choice(["North", "South", "East", "West"], rows),
    "Month": np.random.choice(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], rows),
    "Discount_Rate": np.random.uniform(5, 40, rows).round(2),
    "Online_Promo": np.random.choice(["Yes", "No"], rows),
    "Customer_Rating": np.random.uniform(2.5, 5.0, rows).round(1)
}

# Target variable - Units Sold 
data["Units_Sold"] = (
    0.003 * data["TV_Spend"] +
    0.002 * data["Radio_Spend"] +
    0.001 * data["SocialMedia_Spend"] +
    2 * (data["Online_Promo"] == "Yes").astype(int) +
    np.random.normal(0, 5, rows)
).round(0)

df = pd.DataFrame(data)

# Add missing values
for col in ["TV_Spend", "Influencer_Score", "Customer_Rating"]:
    df.loc[random.sample(range(rows), 5), col] = np.nan

# Add duplicate rows
df = pd.concat([df, df.iloc[[2, 5]]], ignore_index=True)

# Add outliers
df.loc[3, "Radio_Spend"] = 40000
df.loc[6, "Discount_Rate"] = 90

# Save to CSV
df.to_csv("advertising_sales.csv", index=False)
print("Sample dataset 'advertising_sales.csv' created successfully!")