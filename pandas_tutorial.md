
# Introduction to Pandas

* Pandas is a data analysis library that uses the dataframe construct to analyze data.
* It is build on top of Numpy - an important scientific library that uses arrays to handle large datasets.


(FYI): An array is a collection of elements (either values or variables) connected to an array index

## What is a dataframe?

- A dataframe is a two dimensional array that resembles an Excel spreadsheet when printed


    %matplotlib inline
    
    import pandas as pd as a shortcut. We'll see why in the next section
    
    import pandas as pd
    
    used to make plots of our data
    
    import matplotlib

### Getting data into a dataframe


    defining a variable to read a csv file from the web
    twitter_data = pd.read_csv("http://real-chart.finance.yahoo.com/table.csv?s=TWTR&d=6&e=3&f=2015&g=d&a=10&b=7&c=2013&ignore=.csv", header=0)

* twitter_data will be our array index, and the data within the CSV file will become our two dimensional array
* pandas uses dot notation - in the above function, we are telling pandas(pd) to pull its read_csv command
* header=0 tells pandas to view the first row in the CSV file as the header row

### Printing the Head and Tail of our Data


    printing the first five rows, including the header columns
    
    print twitter_data.head()

             Date       Open       High        Low      Close    Volume  Adj Close
    0  2015-07-02  35.400002  35.970001  35.099998  35.720001  17589400  35.720001
    1  2015-07-01  36.049999  36.110001  35.240002  35.400002  23624800  35.400002
    2  2015-06-30  34.500000  36.419998  34.439999  36.220001  25979100  36.220001
    3  2015-06-29  34.470001  35.090000  34.150002  34.209999  25139700  34.209999
    4  2015-06-26  34.970001  35.330002  34.669998  35.259998  16900000  35.259998



    we can also view the last five rows
    
    print twitter_data.tail()

               Date       Open       High        Low      Close     Volume  \
    410  2013-11-13  41.029999  42.869999  40.759998  42.599998    8688300   
    411  2013-11-12  43.660000  43.779999  41.830002  41.900002    6316700   
    412  2013-11-11  40.500000  43.000000  39.400002  42.900002   16113900   
    413  2013-11-08  45.930000  46.939999  40.689999  41.650002   27925300   
    414  2013-11-07  45.099998  50.090000  44.000000  44.900002  117701600   
    
         Adj Close  
    410  42.599998  
    411  41.900002  
    412  42.900002  
    413  41.650002  
    414  44.900002  


### View the entire dataset


    print twitter_data

               Date       Open       High        Low      Close     Volume  \
    0    2015-07-02  35.400002  35.970001  35.099998  35.720001   17589400   
    1    2015-07-01  36.049999  36.110001  35.240002  35.400002   23624800   
    2    2015-06-30  34.500000  36.419998  34.439999  36.220001   25979100   
    3    2015-06-29  34.470001  35.090000  34.150002  34.209999   25139700   
    4    2015-06-26  34.970001  35.330002  34.669998  35.259998   16900000   
    5    2015-06-25  35.360001  35.360001  34.970001  35.169998   10689900   
    6    2015-06-24  35.400002  35.750000  35.099998  35.169998   12959800   
    7    2015-06-23  35.779999  36.200001  34.959999  35.369999   24814600   
    8    2015-06-22  35.950001  36.000000  35.340000  35.549999   21293500   
    9    2015-06-19  34.970001  36.279999  34.849998  35.860001   32923200   
    10   2015-06-18  34.630001  35.040001  34.450001  34.660000   19385800   
    11   2015-06-17  34.990002  35.119999  34.169998  34.689999   27138000   
    12   2015-06-16  34.230000  35.200001  33.509998  34.820000   49591200   
    13   2015-06-15  35.240002  35.259998  34.310001  34.669998   32711500   
    14   2015-06-12  36.900002  37.250000  35.549999  35.900002   60739800   
    15   2015-06-11  35.919998  36.169998  35.790001  35.840000   11090800   
    16   2015-06-10  36.009998  36.169998  35.599998  35.849998   12611800   
    17   2015-06-09  36.500000  36.500000  35.570000  35.880001   13978300   
    18   2015-06-08  36.910000  36.980000  36.410000  36.459999   11718100   
    19   2015-06-05  36.790001  37.230000  36.650002  37.000000   11658700   
    20   2015-06-04  37.169998  37.790001  36.509998  36.709999   23660000   
    21   2015-06-03  36.509998  37.169998  36.480000  37.000000   13806600   
    22   2015-06-02  36.450001  36.599998  36.160000  36.400002   13078400   
    23   2015-06-01  36.689999  36.830002  36.430000  36.630001    9947200   
    24   2015-05-29  37.049999  37.070000  36.529999  36.669998   16515400   
    25   2015-05-28  36.490002  37.330002  36.369999  36.830002   17858900   
    26   2015-05-27  36.500000  36.650002  36.099998  36.410000   14444300   
    27   2015-05-26  36.669998  36.830002  36.369999  36.509998   13026500   
    28   2015-05-22  36.700001  36.980000  36.570000  36.599998    9808800   
    29   2015-05-21  36.810001  36.939999  36.389999  36.680000   17413500   
    ..          ...        ...        ...        ...        ...        ...   
    385  2013-12-19  55.080002  57.750000  55.000000  57.490002   13152500   
    386  2013-12-18  57.000000  57.000000  54.230000  55.509998   16659800   
    387  2013-12-17  56.970001  57.380001  54.619999  56.450001   22115200   
    388  2013-12-16  57.860001  60.240002  55.759998  56.610001   39310800   
    389  2013-12-13  56.200001  59.410000  55.450001  59.000000   38979600   
    390  2013-12-12  52.200001  55.869999  50.689999  55.330002   23446900   
    391  2013-12-11  52.400002  53.869999  51.000000  52.340000   26631500   
    392  2013-12-10  48.900002  52.580002  48.700001  51.990002   25792000   
    393  2013-12-09  45.590000  49.840000  45.020000  49.139999   17366600   
    394  2013-12-06  45.750000  45.799999  44.540001  44.950001    6230000   
    395  2013-12-05  43.450001  46.349998  42.830002  45.619999   11729400   
    396  2013-12-04  41.270000  43.919998  41.270000  43.689999   11014900   
    397  2013-12-03  40.689999  41.599998  40.540001  41.369999    5771000   
    398  2013-12-02  41.790001  42.000000  40.400002  40.779999    6424300   
    399  2013-11-29  41.400002  41.580002  40.900002  41.570000    4107000   
    400  2013-11-27  40.470001  41.400002  40.349998  40.900002    5536300   
    401  2013-11-26  39.160000  40.549999  38.919998  40.180000    9828400   
    402  2013-11-25  41.080002  41.139999  38.799999  39.060001   14333300   
    403  2013-11-22  41.810001  42.279999  40.970001  41.000000    6185200   
    404  2013-11-21  41.250000  42.490002  40.369999  42.060001    8324700   
    405  2013-11-20  41.400002  41.750000  40.509998  41.049999    5767300   
    406  2013-11-19  41.389999  41.900002  40.000000  41.750000    7436600   
    407  2013-11-18  43.500000  43.950001  40.849998  41.139999   12810600   
    408  2013-11-15  45.250000  45.270000  43.430000  43.980000    8010600   
    409  2013-11-14  42.340000  45.669998  42.240002  44.689999   11099400   
    410  2013-11-13  41.029999  42.869999  40.759998  42.599998    8688300   
    411  2013-11-12  43.660000  43.779999  41.830002  41.900002    6316700   
    412  2013-11-11  40.500000  43.000000  39.400002  42.900002   16113900   
    413  2013-11-08  45.930000  46.939999  40.689999  41.650002   27925300   
    414  2013-11-07  45.099998  50.090000  44.000000  44.900002  117701600   
    
         Adj Close  
    0    35.720001  
    1    35.400002  
    2    36.220001  
    3    34.209999  
    4    35.259998  
    5    35.169998  
    6    35.169998  
    7    35.369999  
    8    35.549999  
    9    35.860001  
    10   34.660000  
    11   34.689999  
    12   34.820000  
    13   34.669998  
    14   35.900002  
    15   35.840000  
    16   35.849998  
    17   35.880001  
    18   36.459999  
    19   37.000000  
    20   36.709999  
    21   37.000000  
    22   36.400002  
    23   36.630001  
    24   36.669998  
    25   36.830002  
    26   36.410000  
    27   36.509998  
    28   36.599998  
    29   36.680000  
    ..         ...  
    385  57.490002  
    386  55.509998  
    387  56.450001  
    388  56.610001  
    389  59.000000  
    390  55.330002  
    391  52.340000  
    392  51.990002  
    393  49.139999  
    394  44.950001  
    395  45.619999  
    396  43.689999  
    397  41.369999  
    398  40.779999  
    399  41.570000  
    400  40.900002  
    401  40.180000  
    402  39.060001  
    403  41.000000  
    404  42.060001  
    405  41.049999  
    406  41.750000  
    407  41.139999  
    408  43.980000  
    409  44.689999  
    410  42.599998  
    411  41.900002  
    412  42.900002  
    413  41.650002  
    414  44.900002  
    
    [415 rows x 7 columns]


* Pandas will show the first and last 30 rows to prevent in memory crashes from large datasets

## Creating a Dataframe Subset

We can create a dataframe from our original dataframe! Let's call our new dataframe "snapshot."


    snapshot = twitter_data.head(20)
    
    print snapshot

### Let's Analyze our Data


    snapshot["Volume"]




    0     17589400
    1     23624800
    2     25979100
    3     25139700
    4     16900000
    5     10689900
    6     12959800
    7     24814600
    8     21293500
    9     32923200
    10    19385800
    11    27138000
    12    49591200
    13    32711500
    14    60739800
    15    11090800
    16    12611800
    17    13978300
    18    11718100
    19    11658700
    Name: Volume, dtype: int64



- We create what is called a Series to view a single column

### Viewing a Series within a dataframe


    this will return boolean values, which are not descriptive enough for our analysis
    snapshot["High"] > 36 

### Viewing the data where a certain condition is true


    if we want to find the days where the stock price high is greater than $36 per share, we can display it like so:
    
    snapshot[snapshot.High > 36]


    We find the dates where the Low price is greater than $36 AND the Close price is less than $37
    
    snapshot[(snapshot.Low >= 36) & (snapshot.Close < 37)]

### Sorting data by column


    shortening the twitter_data name
    
    t = twitter_data
    
    find data where the Open price is higher than $65 and sort by Volume
    
    t[t.Open > 65].sort('Volume')




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Adj Close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>355</th>
      <td> 2014-02-04</td>
      <td> 66.250000</td>
      <td> 66.370003</td>
      <td> 64.500000</td>
      <td> 66.320000</td>
      <td> 13017400</td>
      <td> 66.320000</td>
    </tr>
    <tr>
      <th>356</th>
      <td> 2014-02-03</td>
      <td> 65.919998</td>
      <td> 66.480003</td>
      <td> 64.209999</td>
      <td> 65.250000</td>
      <td> 17890300</td>
      <td> 65.250000</td>
    </tr>
    <tr>
      <th>354</th>
      <td> 2014-02-05</td>
      <td> 67.160004</td>
      <td> 67.239998</td>
      <td> 64.800003</td>
      <td> 65.970001</td>
      <td> 31504900</td>
      <td> 65.970001</td>
    </tr>
    <tr>
      <th>374</th>
      <td> 2014-01-07</td>
      <td> 67.669998</td>
      <td> 67.730003</td>
      <td> 61.389999</td>
      <td> 61.459999</td>
      <td> 31748400</td>
      <td> 61.459999</td>
    </tr>
    <tr>
      <th>376</th>
      <td> 2014-01-03</td>
      <td> 69.000000</td>
      <td> 70.430000</td>
      <td> 68.430000</td>
      <td> 69.000000</td>
      <td> 33207200</td>
      <td> 69.000000</td>
    </tr>
    <tr>
      <th>382</th>
      <td> 2013-12-24</td>
      <td> 66.339996</td>
      <td> 70.870003</td>
      <td> 65.559998</td>
      <td> 69.959999</td>
      <td> 35802700</td>
      <td> 69.959999</td>
    </tr>
    <tr>
      <th>380</th>
      <td> 2013-12-27</td>
      <td> 70.099998</td>
      <td> 71.250000</td>
      <td> 63.689999</td>
      <td> 63.750000</td>
      <td> 60418700</td>
      <td> 63.750000</td>
    </tr>
    <tr>
      <th>381</th>
      <td> 2013-12-26</td>
      <td> 72.879997</td>
      <td> 74.730003</td>
      <td> 69.129997</td>
      <td> 73.309998</td>
      <td> 82761100</td>
      <td> 73.309998</td>
    </tr>
  </tbody>
</table>
</div>



### Simple Descriptive Statistics


    basic statistics of our data
    
    t.describe()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Adj Close</th>
      <th>Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td> 415.000000</td>
      <td> 415.000000</td>
      <td> 415.000000</td>
      <td> 415.000000</td>
      <td> 4.150000e+02</td>
      <td> 415.000000</td>
      <td> 415.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>  45.009542</td>
      <td>  45.873084</td>
      <td>  44.066337</td>
      <td>  44.920000</td>
      <td> 2.266575e+07</td>
      <td>  44.920000</td>
      <td>   4.074187</td>
    </tr>
    <tr>
      <th>std</th>
      <td>   8.373991</td>
      <td>   8.613517</td>
      <td>   8.109269</td>
      <td>   8.368144</td>
      <td> 1.646470e+07</td>
      <td>   8.368144</td>
      <td>   2.721641</td>
    </tr>
    <tr>
      <th>min</th>
      <td>  30.940001</td>
      <td>  31.200001</td>
      <td>  29.510000</td>
      <td>  30.500000</td>
      <td> 4.107000e+06</td>
      <td>  30.500000</td>
      <td>   0.932716</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>  38.024999</td>
      <td>  38.695000</td>
      <td>  37.355000</td>
      <td>  37.840000</td>
      <td> 1.309690e+07</td>
      <td>  37.840000</td>
      <td>   2.574163</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>  43.660000</td>
      <td>  44.580002</td>
      <td>  42.509998</td>
      <td>  43.470001</td>
      <td> 1.867650e+07</td>
      <td>  43.470001</td>
      <td>   3.384496</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>  51.019998</td>
      <td>  51.875000</td>
      <td>  50.084999</td>
      <td>  50.825001</td>
      <td> 2.641980e+07</td>
      <td>  50.825001</td>
      <td>   4.780456</td>
    </tr>
    <tr>
      <th>max</th>
      <td>  72.879997</td>
      <td>  74.730003</td>
      <td>  69.129997</td>
      <td>  73.309998</td>
      <td> 1.347100e+08</td>
      <td>  73.309998</td>
      <td>  36.060447</td>
    </tr>
  </tbody>
</table>
</div>



### Append to a dataframe


    Add a column to calculate the percent change from the day's stock low to the day's stock high
    
    t["Change"] = (t.High - t.Low)/t.Low * 100
    print t.head()

             Date       Open       High        Low      Close    Volume  \
    0  2015-07-02  35.400002  35.970001  35.099998  35.720001  17589400   
    1  2015-07-01  36.049999  36.110001  35.240002  35.400002  23624800   
    2  2015-06-30  34.500000  36.419998  34.439999  36.220001  25979100   
    3  2015-06-29  34.470001  35.090000  34.150002  34.209999  25139700   
    4  2015-06-26  34.970001  35.330002  34.669998  35.259998  16900000   
    
       Adj Close    Change  
    0  35.720001  2.478641  
    1  35.400002  2.468782  
    2  36.220001  5.749126  
    3  34.209999  2.752556  
    4  35.259998  1.903675  



   Get mean for all columns in the twitter_data dataframe
   
    t.mean()




    Open               45.009542
    High               45.873084
    Low                44.066337
    Close              44.920000
    Volume       22665748.433735
    Adj Close          44.920000
    Change              4.074187
    dtype: float64




   Get mean for all columns in the snapshot dataframe
   
    snapshot.mean()




    Open               35.548501
    High               35.971500
    Low                35.041500
    Close              35.485000
    Volume       23126900.000000
    Adj Close          35.485000
    dtype: float64



### Merging files to create a large dataframe


    create three new dataframes from three separate csv files
    
    lnkd15_df = pd.read_csv("/Users/moor1204/Desktop/pandas_walkthrough/lnkd_hist2015.csv", header=0)
    lnkd14_df = pd.read_csv("/Users/moor1204/Desktop/pandas_walkthrough/lnkd_hist2014.csv", header=0)
    lnkd13_df = pd.read_csv("/Users/moor1204/Desktop/pandas_walkthrough/lnkd_hist2013.csv", header=0)
    
   combine dataframes into a single list
   
    frames = [lnkd15_df, lnkd14_df, lnkd13_df]
    
    concat the list into a single dataframe
    
    lnkd_full = pd.concat(frames)
    
    print the head and tail to make sure we combined the dataframes correctly
    
    print lnkd_full.head()
    print lnkd_full.tail()

            Date        Open        High         Low       Close   Volume  \
    0   7/7/2015  208.679993  212.440002  203.610001  210.979996  2041600   
    1   7/6/2015  205.380005  209.850006  205.139999  209.449997  1398200   
    2   7/2/2015  208.000000  208.750000  207.059998  207.759995   790200   
    3   7/1/2015  208.869995  209.259995  206.339996  207.960007  1313500   
    4  6/30/2015  205.500000  209.089996  204.979996  206.630005  1591500   
    
        Adj Close  
    0  210.979996  
    1  209.449997  
    2  207.759995  
    3  207.960007  
    4  206.630005  
             Date        Open        High         Low       Close   Volume  \
    247  1/8/2013  112.830002  113.000000  109.800003  111.169998  1252300   
    248  1/7/2013  112.220001  115.180000  111.750000  113.000000  1224900   
    249  1/4/2013  113.000000  113.400002  111.389999  113.150002  1128500   
    250  1/3/2013  112.320000  113.290001  111.120003  112.449997  1302200   
    251  1/2/2013  115.709999  116.330002  110.070000  112.650002  2562400   
    
          Adj Close  
    247  111.169998  
    248  113.000000  
    249  113.150002  
    250  112.449997  
    251  112.650002  





![png](output_36_1.png)



    lnkd_full.to_csv('/Users/moor1204/Desktop/pandas_walkthrough/lnkd.csv')
