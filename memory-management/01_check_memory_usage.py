#Module 01: Check Memory Usage
#Goal: Monitor RAM and object sizes during ML workflows

import psutil
import sys
import pandas as pd
import numpy as np

#1. Check system memory
def check_system_memory():
    mem = psutil.virtual_memory()
    print(f"Total RAM: {mem.total / 1e9:.2f} GB")
    print(f"Available RAM: {mem.available / 1e9:.2f} GB")

#2. Check object size
def check_object_size(obj, name="Object"):
    size = sys.getsizeof(obj)
    print(f"{name} size: {size / 1024:.2f} KB")

#Example usage
df = pd.DataFrame(np.random.rand(1000, 100))
check_system_memory()
check_object_size(df, "DataFrame")

