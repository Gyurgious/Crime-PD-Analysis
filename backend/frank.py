import pandas as pd

# Load Excel file
df = pd.read_excel("NIBRSPublicView2024.xlsx", nrows=2000, usecols=["StreetName", "NIBRSDescription", "Premise", "ZIPCode", "MapLongitude"], dtype={"ZIPCode": str})


# Define the street and crime type you want to check
specific_street = "FUQUA"   # Change to the street name you're looking for
specific_crime = "Theft from motor vehicle"   # Change to the crime type you want to check
premise = "Grocery, Supermarket"

# Filter the dataset
filtered_data = df[(df["StreetName"] == specific_street) & (df["Premise"] == premise)]

crime_count = filtered_data.shape[0]
# Display the filtered results
print(filtered_data)
print(crime_count)
