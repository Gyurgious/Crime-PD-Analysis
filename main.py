import pandas as pd
import os

violent_crimes = ["Aggravated Assault", "Simple assault", "Forcible rape","robbery", "Murder, non-negligent"]

file_1 = "NIBRSPublicView2024.xlsx"
print("test")

df = pd.read_excel(file_1, nrows=10000,usecols=["NIBRSDescription", "ZIPCode", "RMSOccurrenceHour"] , dtype={"ZIPCode": str}) # only processes the first n rows of excel file

# amount of crime at each ZIPCODE
count_crime = df.groupby("ZIPCode")["NIBRSDescription"].count().reset_index()
# Rename the column for clarity
count_crime.columns = ["ZIPCode", "CrimeCount"]
count_crime = count_crime.sort_values(by="CrimeCount", ascending=False)

print(count_crime)
print("yes")

# categorize crime reports into zip codes