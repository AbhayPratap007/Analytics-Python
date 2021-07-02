# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:27:01 2021

@author: Abhay
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('E:/New folder/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('E:/New folder/User_Data.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('E:/New folder/User_Data_Analytics.xlsx')

df1 = pandas.read_excel('User_Data_Analytics.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('User_Data.xlsx')
print (df2)