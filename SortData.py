import pandas as pd
import os
import glob

def filter_dates(dataframe: object):
    dataframe.set_index('Date', inplace = True)
    start_date = input("Enter start date in format MM-DD-YYYY ")
    end_date = input("Enter end date in format MM-DD-YYYY ")
    dataframe = dataframe.loc[start_date:end_date]
    return dataframe

def filter_ticker(dataframe: object):
    dataframe.set_index('Ticker', inplace = True)
    ticker = input("Enter stock ticker ")
    dataframe = dataframe.loc[ticker]
    return dataframe

# Change filepath to your directory
path = "D:\Falling Knife Project\StockData\StockData"
all_files = glob.glob(os.path.join(path, "*Data.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['File'] = f.split('/')[-1]
    df['Ticker'] = df['File'].str.slice(start = 45)
    df['Ticker'] = df['Ticker'].str.slice(stop = -8)
    df['Date'] = pd.to_datetime(df.Date)
    df.sort_values(by = 'Date')  # This now sorts in date order
    all_df.append(df)

merged_df = pd.concat(all_df, ignore_index=True, sort=True)
merged_df1 = filter_dates(merged_df)
merged_df2 = filter_ticker(merged_df1)
print(merged_df2)
#merged_df.to_csv(r'D:\Falling Knife Project\StockData\StockData\MergedData.csv', index = False)