import pandas as pd
import matplotlib
import math
import os
import numpy as np
import random
import cryptpandas as crp
import dotenv
import pyotp

def Anonymize_Dataframe(dataframe):
    df = dataframe
    df.drop(columns = ["SSN"], inplace = True)
    for i in range(len(df["first name"])):
        df.loc[i, "first name"] = random.choice(firstnames)
        df.loc[i, "last name"] = random.choice(lastnames)
def simulate_authentication(key):
   # Simulate the process of authenticating with a TOTP code.
   totp = pyotp.TOTP(key)
   SuccessfulAttempt = False
   print("Enter the code from your Google Authenticator app to complete authentication.")
   user_input = input("Enter Code: ")
   #if totp.verify(user_input):
   print("Authentication successful!")
   dotenv.load_dotenv(r'./env.env')
   SECRET_KEY = os.environ.get("Password")
   crp.to_encrypted(df, SECRET_KEY, r'./test')
   while SuccessfulAttempt == False:
    if totp.verify(user_input):
        decrypted_df = crp.read_encrypted(r'./test', SECRET_KEY)
        decrypted_df.to_excel('./Decryped_File.xlsx', 'PatientInfo')
        # print(decrypted_df)
        #print(SECRET_KEY)
        SuccessfulAttempt = True
    else:
        print("Authentication failed. Please try again with the right key.")

# Main Code
firstnames = ["Jim", "John", "Sue", "William", "Nathan", "Chris", "Ryan", "Sandy",
              "Rachael", "Candis", "Billy", "Bob", "Kelly", "Brianna", "Rebecca",
              "Randy", "Precious", "Barbara", "Heather"]
lastnames = ["Price", "Smith", "King", "Mobley", "Arthur", "Reynolds", "Dion",
             "Carpenter", "Back", "Jones", "Johnson", "Anderson", "Brown",
             "Garcia", "Miller", "Thompson", "Jackson"]
# The key should be the same one generated and used to create the QR code in Program 1
df = pd.read_excel(r'./sample-data.xlsx', sheet_name="Sheet1")
Anonymize_Dataframe(df)
df = df.astype(str)
user_key = open("2fa.txt").read()  # Reading the key from the file generated in Program 1 (otp_qrcode_and_key.py)
simulate_authentication(user_key)
# Read the entire Excel file into a DataFrame
#df = pd.read_excel(r'./sample-data.xlsx', sheet_name="Sheet1")
#df = df.astype(str)
#dotenv.load_dotenv(r'./env.env')
#SECRET_KEY = os.environ.get("Password")
#crp.to_encrypted(df, "hello", r'./test')
#decrypted_df = crp.read_encrypted(r'./test', "hello")
#print(decrypted_df)
#print(SECRET_KEY)