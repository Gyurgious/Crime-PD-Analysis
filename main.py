import pandas as pd
import os

violent_crimes = ["Aggravated Assault", "Simple assault", "Forcible rape","robbery", "Murder, non-negligent"]

file_1 = "NIBRSPublicView2024.xlsx"
print("test")

df = pd.read_excel(file_1, nrows=300,usecols=["NIBRSDescription", "ZIPCode", "RMSOccurrenceHour"]) # only processes the first n rows of excel file

print(df)
print("yes")