import pandas as pd
import os

violent_crimes = ["Aggravated Assault", "Simple assault", "Forcible rape","Robbery", "Murder, non-negligent"]
public_order_crimes = ["Disorderly conduct"]
drug_narcotic_crimes = ["Drug, narcotic violations"]
burglary_crimes = ["Burglary, Breaking and Entering"]

file_1 = "NIBRSPublicView2024.xlsx"
print("test")

df = pd.read_excel(file_1, nrows=10000,usecols=["NIBRSDescription", "ZIPCode", "RMSOccurrenceHour"] , dtype={"ZIPCode": str}) # only processes the first n rows of excel file

# amount of crime at each ZIPCODE
count_total_crime = df.groupby("ZIPCode")["NIBRSDescription"].count().reset_index()
count_total_crime.columns = ["ZIPCode", "Total Crime Count"] # Rename the column for clarity
count_total_crime = count_total_crime.sort_values(by="Total Crime Count", ascending=False) # sort crime reports 



# Count crimes per ZIP code and type
crime_counts_by_type = df.groupby(["ZIPCode", "NIBRSDescription"]).size().reset_index(name="Crime Count")

# Sort within each ZIP code by highest crime type
crime_counts_by_type = crime_counts_by_type.sort_values(by=["ZIPCode", "Crime Count"], ascending=[True, False])


highest_crime = 0
ABUNAI_ZIPCODE = ""
for zipcode in crime_counts_by_type["ZIPCode"].unique():
    total_crime = count_total_crime[count_total_crime["ZIPCode"] == zipcode]["Total Crime Count"].values[0]
    if total_crime > highest_crime:
        highest_crime = total_crime
        ABUNAI_ZIPCODE = zipcode

    print(f"\n ZIP Code: {zipcode} - Total Crime: {total_crime}")
    crimes_in_zip = crime_counts_by_type[crime_counts_by_type["ZIPCode"] == zipcode]
    for _, row in crimes_in_zip.iterrows():
        print(f"   - {row['NIBRSDescription']}: {row['Crime Count']} crimes")



# print(count_total_crime)
print(f"\n Most dangerous area is {ABUNAI_ZIPCODE} with {highest_crime} crimes")

# categorize crime reports into zip codes