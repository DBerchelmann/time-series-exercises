# import libraries

import pandas as pd
import requests
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import seaborn as sns

#import data set

from vega_datasets import data
from io import StringIO
from acquire import items_, stores_, sales_, merge_dataframes, pull_csv







def prep_store():
    
    '''
    This function merges several tables and then converts the date to datetime datatype and sets
    it as the index. A day and month column are then created followed by a column create of total sales.
    '''
 
    df = merge_dataframes()
    
    # convert date to date/time and set as index
    
    df.sale_date = pd.to_datetime(df.sale_date)
    df = df.set_index('sale_date').sort_index()
    df.index = df.index.tz_localize(None)
    
    # Add day column
    
    df['day'] = df.index.day_name()
    
    # Add month column
    
    df['month'] = df.index.month_name()
    
    # Add total sales column
    
    df['sales_total'] = df.item_price * df.sale_amount
    
    return df










def prep_csv():
    
    '''
    This function pulls a .csv from a specified URL and returns a dataframe. It then converts the date to datetime datatype and sets
    it as the index. A month and year column are then created followed by code that fills any NaNs with zero
    '''
    
    
    df = pull_csv("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")
    
    # convert date to date/time and set as index
    
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date').sort_index()
    
    # Add month column
    
    df['month'] = df.index.month_name()
    
    # Add year column
    
    df['year'] = pd.DatetimeIndex(df.index).year
    
    # Fill NaNs with zero
    
    df.fillna(0, inplace=True)
    
    return df

def plot_variables():
    
    '''
    This function creates a historgram for every variable in the dataframe
    '''
    
    df = prep_csv()
    
      
    fig = plt.figure(figsize = (12,8))
    
    ax = fig.gca()
    
    df.hist(ax = ax, bins = 8)