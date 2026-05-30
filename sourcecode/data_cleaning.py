import pandas as pd;



df=pd.read_csv("source data/CPIH.csv", skiprows=5,nrows=23)
df = df.drop(columns=["Unnamed: 0"," average"])
df = df.dropna(axis=0, how="all")
df=df.drop([0])

#df=df.fillna(None)
df=df.rename(columns={"Unnamed: 1": "Year"})

melted_df=pd.melt(df,id_vars=["Year"],var_name="Month",value_name="CPI")
melted_df["CPI"] = pd.to_numeric(melted_df["CPI"], errors="coerce")
melted_df["Month"] = melted_df["Month"].str.strip()
# Create a combined date string (e.g., "Jan 2005")
melted_df["Date"] = melted_df["Month"] + " " + melted_df["Year"].astype(str)

# Convert the string into a true Pandas Datetime object
melted_df["Date"] = pd.to_datetime(melted_df["Date"], format="%b %Y")

# Sort the values chronologically (melting often messes up the original time order)
melted_df = melted_df.sort_values("Date").reset_index(drop=True)

# Check your new Date column!
print(melted_df.head())
#print(df)
#print(df.columns)
#print(melted_df["CPI"].dtype)
#print(melted_df["CPI"].max())
#print(melted_df.loc[melted_df["CPI"].idxmax()])