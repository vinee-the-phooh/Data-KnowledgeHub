#Module 02: Clear Memory by Deleting Objects
#Goal: Free up memory manually when objects are no longer needed

import pandas as pd
import numpy as np
import gc  # Garbage Collector

#Create large object
df = pd.DataFrame(np.random.rand(1000000, 10))

#Delete object
del df

#Run garbage collector
gc.collect()
print("Memory cleared!")

