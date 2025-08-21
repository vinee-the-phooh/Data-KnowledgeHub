"""
===============================================================================
My Learning Note: From Python List -> NumPy -> Pandas -> DataFrame
For non-native English speakers and beginners in ML / Data Science
===============================================================================

WHY THIS FILE?
--------------
This file is a simple guide. It shows how we move data in steps:
1) Python list  (basic container)
2) NumPy array  (easy math, fast)
3) Pandas Series (one labeled column)
4) Pandas DataFrame (table, many columns)

Simple Flow:
    Python list
        |  (convert)
    NumPy array
        |  (add labels)
    Pandas Series
        |  (add more columns)
    Pandas DataFrame

WHY EACH STEP?
--------------
- Python list: easy to start, but not good for math on all items.
- NumPy array: good for math (vectorized). Example: add 10 to all numbers.
- Pandas Series: like one column in Excel, with index (row labels).
- Pandas DataFrame: like an Excel table (many columns). Best for analysis.

IMPORTANT WORDS
---------------
- Vectorized: do math on the whole array/column without writing loops.
- Index: row labels in Pandas (0,1,2,... by default).
- Column: a Series inside a DataFrame.
- Name (in Series): a label you give to the column, like "Age" or "Score".

TIP: Run this file step by step and read the outputs.
"""

import numpy as np
import pandas as pd


def step_1_python_list():
    """
    Step 1: Python list
    - Basic container in Python.
    - Good for storing values.
    - Not good for fast math on many values.
    """
    py_list = [1, 2, 3, 4]
    print("STEP 1 — Python list:", py_list)
    print("Access first item (index 0):", py_list[0])
    print("Sum of list (built-in):", sum(py_list))
    doubled = [x * 2 for x in py_list]
    print("List comprehension (x*2):", doubled)
    return py_list


def step_2_numpy_array(py_list):
    """
    Step 2: NumPy array
    - Best for math and statistics.
    - Vectorized operations (fast).
    """
    np_array = np.array(py_list)
    print("\nSTEP 2 — NumPy array:", np_array)
    print("Add 10 to all items:", np_array + 10)
    print("Mean:", np_array.mean(), "  Std:", np_array.std())
    print("Element-wise square:", np_array ** 2)
    return np_array


def step_3_pandas_series(py_list):
    """
    Step 3: Pandas Series
    - One labeled column (like one Excel column).
    - Has index (row labels).
    - Name is like the "column header".
    """
    series = pd.Series(py_list, name="numbers")
    print("\nSTEP 3 — Pandas Series:\n", series)

    # Explanation of parts:
    print("\n--- Understanding Series ---")
    print("Values only:", series.values)  # like [1,2,3,4]
    print("Index labels:", list(series.index))  # row labels, default [0,1,2,3]
    print("Name of Series:", series.name)  # "numbers"

    print("\nSo this means:")
    print("Index = row labels (0,1,2,3 by default)")
    print("Name = column header (like 'numbers')")
    return series


def step_4_pandas_dataframe(py_list, np_array):
    """
    Step 4: Pandas DataFrame
    - A table with many columns (many Series together).
    """
    df = pd.DataFrame({
        "numbers": py_list,          # from Python list
        "squares": np_array ** 2,    # from NumPy math
        "plus_ten": np_array + 10,
    })
    print("\nSTEP 4 — Pandas DataFrame:\n", df)
    print("Columns:", list(df.columns))
    print("Shape (rows, cols):", df.shape)
    return df


def demo_flow():
    """
    Run all steps in order so you can see the journey:
    Python list -> NumPy array -> Pandas Series -> Pandas DataFrame
    """
    py_list = step_1_python_list()
    np_array = step_2_numpy_array(py_list)
    _series = step_3_pandas_series(py_list)
    _df = step_4_pandas_dataframe(py_list, np_array)


if __name__ == "__main__":
    demo_flow()