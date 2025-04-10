import pandas as pd
from api.models import CrimeRecord  # You'll create this model
from django.db import transaction

df = pd.read_excel("NIBRSPublicView2024.xlsx", usecols=["ZIPCode", "NIBRSDescription"], dtype={"ZIPCode": str})

# Clean and count
count_total_crime = df.groupby("ZIPCode")["NIBRSDescription"].count().reset_index()
count_total_crime.columns = ["ZIPCode", "TotalCrime"]

# Save to DB
@transaction.atomic
def load_data():
    for _, row in count_total_crime.iterrows():
        CrimeRecord.objects.create(zipcode=row["ZIPCode"], total_crime=row["TotalCrime"])

load_data()
