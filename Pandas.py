# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:25:24 2021

@author: Singh
"""

#-------------Pandas---------------

import pandas as pd

mydataset = {"Books":["The Alchemist","The Art of Happiness","The gift from the sea"],
             "Ratings": [4.7,4.7,4.6]}
data = pd.DataFrame(mydataset)
print(data)

#---------------Checinkg Pandas version--------------

print(pd._version_)

#--------------Series--------------
#Create a simple Pandas Series from list

s = pd.Series([1.,2.,3.])
print(s)
print(s[0]) #label or index

#Create Labels
s = pd.Series([1.,2.,3.],index=["a","b","c"])
# add the index with index. It helps to name the rows. The length should be equal to the size of the column
print(s)

# Create a simple Pandas Series from a dictionary
bookdata = {"item1":"The Alchemist","item2":"The Art of Happiness","item3":"Teh Gift from Sea"}
data = pd.Series(bookdata)
#Note: The keys of the dictionary become the labels
print(data)

#To select only some of the items in the dictionary, use the index argument
bookdata = {"item1":"The Alchemist","item2":"The Art of Happiness","item3":"Teh Gift from Sea"}
data = pd.Series(bookdata,index = ["item1","item2"])
print(data)

#-----------------Pandas DataFrame--------------
#Create a DataFrame from two Series:
data = {"Classes":["Mathematics","Chemistry","Physics","History","Geography"],    
        "Grades" : [90,54,77,22,25]} 
df = pd.DataFrame(data)
print(df)
# return row 0
print(df.loc[0]) # This example return pandas Series

# return row 0 and 1
print(df.loc[[0,1]])

#Add a list of names to give each row a name:
new_df = pd.DataFrame(data,index=["Subject1","Subject","Subject3","Suject4","Subject5"])
print(new_df)

print(new_df.loc["Subject3"]) # Return "Subject3"

#Load files into a Dataframe
df = pd.read_csv("Purchase_History.csv")

#Read CSV Files
df = pd.read_csv("Purchase_History.csv",encoding='unicode_escape')
df

#------------Analyzing DataFrames------------------
#I will read the data from the .csv file and perform the following basic operations on movies data
#1. Read data 
#2. View the data 
#3. Understand some basic information about the data
# 4. Data Selection – Indexing and Slicing data 
#5. Data Selection – Based on Conditional filtering
#6. Groupby operations 
#7. Sorting operation 
#8. Dealing with missing values 
#9. Dropping columns and null values 
#10. Apply( ) functions

data = pd.read_csv("IMDB-Movie-Data.csv")
#read data with specified explicit index.
#We will use this later in our analysis
data_indexed = pd.read_csv("IMDB-Movie-Data.csv",index_col='Title')
data_indexed

data.head() #view data top 5
data.tail() #bottom 5
data.info() #information about data
data.shape #check size
data.describe() # basic statistical summaries of all numerical attributes in the dataframe

#------------Data Selection-Indexing and Slicing----------
genre = data["Genre"]

#Extract data as dataFrame
data[["Genre"]]

#If we want to extract multiple columns from the data, simply add the column names to the list.
cols = data[['Title','Genre','Actors','Director','Rating']]
cols
#loc – locates the rows by name 
data_indexed.loc[["Captain America: Civil War"]][['Genre','Actors','Director','Rating','Revenue (Millions)']]
#iloc performs slicing based on Python’s default numerical index
data_indexed.iloc[15:20][["Director","Rating","Revenue (Millions)"]]

# Data Selection – Based on Conditional Filtering 
data[((data['Year'] >= 2010) & (data['Year'] <= 2016))
     & (data['Rating'] < 6.0)
     & (data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))]
#'‘The Twilight Saga: Breaking Dawn – Part 2′ and ‘The Twilight Saga: Eclipse’ are the movies that topped in the box office, despite having lower ratings.'

#----------------Groupby--------------

data.groupby("Director")[["Rating"]].mean().head()

#--------------- Sorting Operation ------------
#sort_values( ) method is used to perform sorting operation on a column or a list of multiple columns

data.groupby("Director")[["Rating"]].mean().sort_values(["Rating"],ascending=False).head()

#-------------------- Dealing with missing values-------

#to check null values
data.isnull().sum()

#------------------- Dropping columns and null values ----------

data.drop('Metascore',axis=1)

#drop all rows containing missing data
data.dropna()

#drop all columns containing missing data
data.dropna(axis=1)

#fillna( ) –> function used to fill null values with specified values
rev_mean = data_indexed["Revenue (Millions)"].mean()
print(rev_mean)
#fill null values with this mean revenue
data_indexed["Revenue (Millions)"].fillna(rev_mean,inplace=True)

#------------------- Apply() function -----
#classify movies based on ratings

def rating_group(rating):
    if rating>=7.5:
        return "Good"
    if rating>=6.0:
        return "Average"
    else:
        return "Bad"
    
#creating a new variable in the dataset to hold the rating category
data['Rating_category']=data['Rating'].apply(rating_group)
 
data[['Title','Director','Rating','Rating_category']].head(10)