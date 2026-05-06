import pandas as pd
from sqlalchemy import create_engine

file_path = "C:/temp/cleaned_sales.csv"

# STEP 1: READ CSV
df = pd.read_csv(file_path, engine="python")

# STEP 2: FIX SINGLE COLUMN ISSUE (if any)
if df.shape[1] == 1:
    df = df.iloc[:, 0].str.split(",", expand=True)

# STEP 3: REMOVE FULLY EMPTY COLUMNS (IMPORTANT FIX)
df = df.dropna(axis=1, how="all")

# STEP 4: REMOVE LAST 2 JUNK COLUMNS IF EMPTY
df = df.loc[:, ~df.columns.isna()]

# STEP 5: KEEP ONLY FIRST 23 COLUMNS (CLEAN STRUCTURE)
df = df.iloc[:, :23]

# STEP 6: PROPER COLUMN NAMES
df.columns = [
    "Row_ID","Order_ID","Order_Date","Ship_Date","Ship_Mode",
    "Customer_ID","Customer_Name","Segment","Country_Region","City",
    "State_Province","Postal_Code","Region","Product_ID","Category",
    "Sub_Category","Product_Name","Sales","Quantity","Discount",
    "Profit","Month","Year"
]

# STEP 7: CLEAN NULLS
df = df.fillna(0)

# STEP 8: MYSQL CONNECTION
engine = create_engine(
    "mysql+mysqlconnector://root:Lankapalli%4012@localhost/sales_project"
)

# STEP 9: LOAD DATA
df.to_sql("sales", con=engine, if_exists="replace", index=False)

print("🎉 CLEAN DATA IMPORT SUCCESSFUL!")