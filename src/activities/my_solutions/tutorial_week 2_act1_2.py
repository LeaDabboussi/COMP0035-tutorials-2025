import pandas as pd
from importlib.resources import files
paralympics_raw_csv = files("activities.data").joinpath("paralympics_raw.csv")
paralympics_raw_xlsx = files("activities.data").joinpath("paralympics_all_raw.xlsx")

# Read content os the files
paralympic_csv = pd.read_csv(paralympics_raw_csv)
paralympic_xlsx = pd.read_excel(paralympics_raw_xlsx, sheet_name=0) # reads worksheet 1 of excel workbook

