#Module 03: Batch Processing
#Goal: Process data in chunks to avoid memory overload

import pandas as pd

#Simulate large CSV
# df = pd.read_csv("large_file.csv")  # Not memory-safe

#Use chunksize
for chunk in pd.read_csv("large_file.csv", chunksize=10000):
    print("Processing chunk...")
    # Do something with chunk
    print(chunk.head())

