#Module 05: NumPy Memory Tips
#Goal: Use memory-efficient NumPy techniques

import numpy as np

#Use float32 instead of float64
arr = np.random.rand(1000000).astype(np.float32)
print("Array dtype:", arr.dtype)
print("Size:", arr.nbytes / 1e6, "MB")

