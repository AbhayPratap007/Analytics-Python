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

 #print pattern
n = 6
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end='')
    print()
    
#Number Pattern
n = 5
for i in range(n+1):
    for j in range(i):
            print(i,end='')
    print()
    
#Half pyramid pattern with the number
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

#Multiplication Number in column
n = int(input("Enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end='')
    print()
    
#Don't do this way
name = "Abhay !!"
print("Hello, my name is",name)
#Do this way
name = "Abhay !!"
print(f"Hello, my name is {name}")
 
