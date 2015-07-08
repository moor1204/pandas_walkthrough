

    #used to make plots of our data
    import matplotlib
    
    #we'll use this library to do some basic arithmetic 
    import numpy as np
    
    import pandas as pd


    #defining a variable to read a csv file from the web
    twitter_data = pd.read_csv("http://real-chart.finance.yahoo.com/table.csv?s=TWTR&d=6&e=3&f=2015&g=d&a=10&b=7&c=2013&ignore=.csv", header=0)


    #printing the first five rows, including the header columns
    print twitter_data.head()


    #we can also view the last five rows
    print twitter_data.tail()


    print twitter_data


    snapshot = twitter_data.head(21)
    print snapshot


    # this will return boolean values, which are not descriptive enough for our analysis
    snapshot["High"] > 36 


    #if we want to find the days where the stock high is greater than $36 per share, we can display it like so:
    snapshot[snapshot.High > 36]


    #We find the dates where the Low price is greater than $36 AND the Close price is greater than $35
    snapshot[(snapshot.Low >= 36) & (snapshot.Close <= 37)]


    #find data where the Open price is higher than $65 and sort by Volume
    t = twitter_data
    t[t.Open > 65].sort('Volume')


    #basic statistics of our data
    t.describe()


    #Add a column to calculate the percent change from the day's stock low to the day's stock high
    t["Change"] = (t.High - t.Low)/t.High * 100
    print t["Change"]


    t.mean()


    snapshot.mean()


    
