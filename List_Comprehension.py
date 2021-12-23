# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:19:58 2021

@author: Singh
"""

#---------List comprehension------------

#Ex1.
my_list = [1,2,3,4]
my_list.append(5)
print(my_list)

#Ex2.
for value in range(5,9):
    my_list.append(value)
print(my_list)

#Ex3.
#create a list of charcharters in your name using list comprehension
my_str = "Canitech"
my_list = [char for char in my_str]
print(my_list)

#Ex4.
num_list = [num for num in range(1,20)]
print(num_list)

#Ex5.
#Divide the num_list into even_list and odd_list
even_list = [num for num in num_list if num%2==0]
print(even_list)
odd_list=[num for num in num_list if num%2==1]
print(odd_list)

#Ex6.
#Create a even-squared in list from num_list
even_square = [num**2 for num in num_list if num%2==0]
print(even_square)

#Ex7.
num_2 = [num+2 for num in num_list]
print(num_2)

#Covert list to dictionary
#Ex1
#Using fromkeys() function
fruits = ['Apple','Pear','Peach','Banana']
fruit_dictionary = dict.fromkeys(fruits,'In stock')
print(fruit_dictionary)

#Ex2
#Using zip() function
fruits = ["Apple","Pear","Peach"]
prices = [0.35,0.40,0.28]
fruit_dictionary = dict(zip(fruits,prices))
print(fruit_dictionary)
