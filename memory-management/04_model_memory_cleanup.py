#Module 04: Model Memory Cleanup
#Goal: Free memory after training ML models

from sklearn.linear_model import LogisticRegression
import numpy as np
import gc

#Train model
X = np.random.rand(10000, 10)
y = np.random.randint(0, 2, size=10000)
model = LogisticRegression()
model.fit(X, y)

#Delete model and data
del model, X, y
gc.collect()

print("Model and data cleared from memory")

