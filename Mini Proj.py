# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:44:43 2021

@author: Singh
"""

#create imojies
print("\U0001F600")
print("\U0001F618")
print("\U0001F637")
print("\U0001F917")
print("\U0001F62A")

#print Pattern in reverse
rows = 5
for i in range(rows+1,0,-1):
  for j in range(0,i-1):
    print("*",end=" ")
  print(" ")
