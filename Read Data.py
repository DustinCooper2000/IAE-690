import pandas as pd
import matplotlib
import math
import os
import numpy as np
import xlrd
# Read the entire Excel file into a DataFrame
df = pd.read_excel(r'./sample-data.xlsx', sheet_name="Sheet1")
print(df)