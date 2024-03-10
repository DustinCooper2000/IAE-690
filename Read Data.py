import pandas as pd
import matplotlib
import math
import os
import numpy as np
import xlrd
import cryptpandas as crp
import dotenv
# Read the entire Excel file into a DataFrame
df = pd.read_excel(r'./sample-data.xlsx', sheet_name="Sheet1")
df = df.astype(str)
dotenv.load_dotenv(r'./env.env')
SECRET_KEY = os.environ.get("Password")
crp.to_encrypted(df, "hello", r'./test')
decrypted_df = crp.read_encrypted(r'./test', "hello")
#print(decrypted_df)
print(SECRET_KEY)