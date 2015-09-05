
# coding: utf-8

# # Pandas for Financial Data Analysis

# ###What is Pandas?

# Pandas is a data analysis library built on Numpy.

# ###Pandas Features
# 
# - Database-like tables with cells and columns
# - Dataframes (two dimensional arrays)
# - Data cleaning: can remove duplicates, manage missing values, align tables by index
# - Create "pivot tables" 
# - SQL operators such as "Join" and "Group By"
# - Can handle CSV, Excel, txt files
# - Export data to CSV 
# - inline data visualization featuring Matplotlib

# In[2]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas.io.data as web
import datetime


# *Quick note: io.data subpackage will be depricated in Pandas version 0.17. Use with caution!

# ###Let's Get Started

# There are a few ways to import data into Pandas:
#     * Local files
#     * Remote files
#     * Remote Data Access (using the pandas.io API)

# ####Pandas.io API

# * use an API to retrieve historical data from SP500
# * use API to retrieve specific date's stock price

# In[3]:

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2015, 8, 24)

sp500 = web.DataReader("%5EGSPC", 'yahoo', start, end)

sp500.head()


# In[4]:

ts = sp500[["Open", "Close"]][-10:]

ts


# We can retrieve any historical data for stocks listed on Yahoo!Finance

# In[5]:

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2015, 8, 24)

ford = web.DataReader("F", 'yahoo', start, end)

ford.head()


# ###Yahoo! API

# Type the following into your web browser:
#     
#     http://chartapi.finance.yahoo.com/instrument/1.0/F/chartdata;type=quote;range=1y/csv

# ###Let's take a look at downloading files from the web:

# What types of files can we import into Pandas?

# ###Tab completion 

# In[3]:

pd.read_<TAB>


# - tab completion will display all of the functions available to you. 

# In[6]:

get_ipython().magic('pinfo pd.read_csv')


# - Displays documentation for a function

# ###Read a CSV file from the Web

# In[7]:


twitter_data = pd.read_csv("http://real-chart.finance.yahoo.com/table.csv?s=TWTR&d=8&e=24&f=2015&g=d&a=10&b=7&c=2013&ignore=.csv", 
                           header=0, index_col="Date")


# #### Print the first five rows of our dataset using the Head function

# In[8]:

twitter_data.head()


# ####Print the last ten rows of our dataset using the Tail function

# In[9]:

twitter_data.tail(10)


# ####View the entire dataset

# In[10]:

twitter_data


# ####A few things to note:
# - Pandas will print the first 30 and last 30 rows by default to save memory
# - Once printed, Pandas will provide a summary of the rows and columns in the dataframe
# - Pandas assigns row numbers to the dataset
# - The header row is excluded in the total row count

# ###We can make new dataframes from a subset of our original data

# In[11]:

snapshot = twitter_data[2:24]
snapshot


# ###Let's Analyze Our Data

# In[80]:

snapshot["Volume"]


# ####Note that:
# 
# - Columns are indexed
# - Returns the "Volume" column, and provides the data type at the end 
# - A single column can also be subset as a Series (a one dimensional array with axis labels)

# ###Viewing Data Based on a Condition

# In[81]:

snapshot["High"] > 36 


# #### This will return boolean values, which are not descriptive enough for our analysis...
# 
# * we want to view the full dataset that meets our condition

# ####If we want to find the days where the stock price high is greater than $36 per share, we can display it like so:

# In[12]:

snapshot[snapshot.High > 36]


# ####We find the dates where the Low price is greater than 36 dollars per share AND the Close price is less than 37

# In[13]:

snapshot[(snapshot.Low >= 36) & (snapshot.Close < 37)]


# ###Going back to our original dataframe...

# ####The Sort function

# ####Find data where the Open price is higher than 65 dollars per share and sort by Volume

# In[15]:

t = twitter_data


t[t.Open > 65].sort('Volume')


# #### Basic Descriptive Statistical Analysis of our dataframe

# In[16]:

t.describe()


# ###Simple calculations and appending a dataframe

# ####Add a column to calculate the percent change from the day's stock low to the day's stock high

# In[17]:


t["Change"] = (t.High - t.Low)/t.Low * 100
t.head()


# In[18]:

close = t['Adj Close']
ma = pd.rolling_mean(close, 50)

ma[-50:]


# ###Merging CSV Files

# ####Create three new dataframes from three separate csv files

# In[19]:

lnkd15_df = pd.read_csv("C:\\Users\\Melodie.Wilson\\Desktop\\pandas_walkthrough\\lnkd_hist2015.csv", header=0, index_col="Date")
lnkd14_df = pd.read_csv("C:\\Users\\Melodie.Wilson\\Desktop\pandas_walkthrough\\lnkd_hist2014.csv", header=0, index_col="Date")
lnkd13_df = pd.read_csv("C:\\Users\\Melodie.Wilson\\Desktop\\pandas_walkthrough\\lnkd_hist2013.csv", header=0, index_col="Date")


# ####Combine dataframes into a single list

# In[20]:

frames = [lnkd15_df, lnkd14_df, lnkd13_df]


# ####Concat the list into a single dataframe

# In[21]:

lnkd_full = pd.concat(frames)


# In[22]:

get_ipython().magic('pinfo pd.concat')


# ####Print the head and tail to make sure we combined the dataframes correctly

# In[23]:

lnkd_full.head()


# In[24]:

lnkd_full


# In[25]:

lnkd15_df


# In[92]:

lnkd_full.to_csv("C:\\Users\\Melodie.Wilson\\Desktop\\merged.csv", header=True)


# ###What if my data is a little more messy?

# * Pandas can exclude rows that we don't want included in our dataset

# In[26]:

axp_data = pd.read_table("C:\\Users\\Melodie.Wilson\\Desktop\\pandas_walkthrough\\axp_hist.csv", 
                         sep=",", skiprows=8, engine="python", parse_dates=[[0,1]], index_col=0)


# In[27]:

axp_data.head(10)


# ####The read_table function

# In[28]:

get_ipython().magic('pinfo pd.read_table')


# ##Plotting our Data

# * use matplotlib inline to display plots of our data directly into the notebook

# In[29]:

t.plot(figsize=(12, 8))


# * data is not easy to read. Let's add some parameters to make sense of our data

# In[30]:

t.plot(subplots=True, figsize=(16, 12))


# ####Histograms of an individual column within a datframe

# In[31]:

t["Adj Close"].plot(kind='hist', stacked=True, bins=20, figsize=(10,8), color='b')


# In[32]:

t["Volume"].plot(kind='hist', stacked=True, bins=20, figsize=(12,8), color='m')


# In[33]:

plt.style.use('dark_background')


sp500["Adj Close"].plot(figsize=(16, 12))
plt.xlabel('Year')
plt.ylabel('Price')
plt.title('S&P500 2010-2015')

plt.show()


# In[34]:

ax1 = plt.subplot(2, 1, 1)
ax1.plot(close, label="sp500")
ax1.plot(ma, label="50MA")
plt.legend()

ax2 = plt.subplot(2, 1, 2)
ax2.plot(sp500["High"], label = "High")
plt.legend()
plt.show()


# In[35]:

axp_close = axp_data['Close'][-50:]
moving_average = pd.rolling_mean(axp_close, 50)

ma[-50:]


# In[144]:

ax1 = plt.subplot(2, 1, 1)
ax1.plot(axp_close, label="AXP Historical Stock Data")
plt.legend()

ax2 = plt.subplot(2, 1, 2)
ax2.plot(axp_data["Volume"], label = "Volume")
plt.legend()
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:




# #Pandas for Financial Data Analysis

# ##Thank you!
