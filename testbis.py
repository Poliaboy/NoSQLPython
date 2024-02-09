import pandas as pd

# Read data from file 'flattened_stocks.json'
# (in the same directory that your python process is based)
data = pd.read_json("/Users/alexs/Documents/NoSQL/Rendu_Cass/stocks_clean.json", lines=True)

data = data.fillna('N/A')
data.replace('N/A', pd.NA, inplace=True)

# Preview the first 5 lines of the loaded data
print(data.head())

# Saving the data to csv
data.to_csv("/Users/alexs/Documents/NoSQL/Rendu_Cass/stocks.csv", index=False)
