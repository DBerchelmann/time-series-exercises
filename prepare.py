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


def prep_csv():
    
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
    
    df = prep_csv()
    
      
    fig = plt.figure(figsize = (12,8))
    
    ax = fig.gca()
    
    df.hist(ax = ax, bins = 8)