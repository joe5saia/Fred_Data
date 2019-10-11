###############################################################################
"""  
pull_fred.py
Author: Joe Saia

Description: This scripts pulls data from FRED. The series to be pulled are 
specified in the main. Functions are a bit overworked so that you can build them
out if you need to do more complicated data pulls like merging series.

Inputs: None.

Outputs: /app/output/freddata.csv contains the series. 

FRED Key: If you plan on using this repeatedly, please use a new API key.
You can get one in less than 30 seconds from the St Louis Fed website below.
Once you have your own you do not need to worry about a lock out for a key. 
https://research.stlouisfed.org/docs/api/api_key.html
"""
###############################################################################

import pandas as pd
from fredapi import Fred

def freddata(fred, series):
    ################################################################################
    # Download data from FRED
    # inputs: fred is a Fred object from the fredapi module
    # series is a list of series to pull from FRED
    ################################################################################
    print('Reading in Fred data')
    data = pd.DataFrame({s: fred.get_series(s) for s in series})
    return data

def runfreddata(fred, series, outfile):
    ################################################################################
    # Calls freddata and then cleans names and saves 
    # inputs: fred is a Fred object from the fredapi module
    # series is a list of series to pull from FRED
    # outfile is where the file should be saved 
    ################################################################################
    df = freddata(fred,series)
    df.columns = map(str.upper, df.columns)
    df.to_csv(outfile, index_label = 'DATE')

def main():
    # Run everything 
    ## Replace below your FRED API key
    fred = Fred('5240bbe3851ef2d1aaffd0877d6048dd')
    series = ['CPIAUCSL']
    runfreddata(fred, series, '/app/output/freddata.csv')


main()

