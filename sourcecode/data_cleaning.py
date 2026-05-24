import pandas as pd;



df=pd.read_csv("source data/CPIH.csv", skiprows=5,nrows=23)
df = df.drop(columns=["Unnamed: 0"," average"])
df = df.dropna(axis=0, how="all")
df=df.drop([0])

#df=df.fillna(None)
df=df.rename(columns={"Unnamed: 1": "Year"})

melted_df=pd.melt(df,id_vars=["Year"],var_name="Month",value_name="CPI")


#print(df)
#print(df.columns)
print(melted_df)