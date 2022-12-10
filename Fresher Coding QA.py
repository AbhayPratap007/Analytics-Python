# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:50:33 2022

@author: ankit
"""

#------------Python Coding Interview Questions For Freshers----------------

#----------------Write a Python Code to Check if a Number is Odd or Even.---------

num1 = int(input("Enter a number:"))

if (int(num1) % 2) == 0:  
    print("{0} is Even number".format(num1))  
else:  
   print("{0} is Odd number".format(num1))  

#-----------------Write a Python code to find the maximum of two numbers.---------------

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
maximum = max(int(num1), int(num2))
print("The maximum number is: ",maximum)

#---------------Write a Python code to check prime numbers.------------------

# Function to check prime number  
def PrimeChecking(num):  
    # Condition to check given number is more than 1  
    if num > 1:  
        # For look to iterate over the given number  
        for i in range(2, int(num/2) + 1):  
            # Condition to check if the given number is divisible  
            if (num % i) == 0:  
                #If divisible by any number it's not a prime number
                print("The number",num, "is not a prime number")  
                break  
        # Else print it as a prime number  
        else:  
            print("The number",num, "is a prime number")  
    # If the given number is 1  
    else:  
        print("The number",num, "is not a prime number")  
# Input function to take the number from user  
num = int(input("Enter a number to check prime or not: "))  
# To print the result, whether a given number is prime or not  
PrimeChecking(num)  

#-----------------Write a Python factorial program without using if-else, for, and ternary operators.-----------

#importing the math function
import math

#Defining the factorial() function to find factorial
def factorial(num):
	return(math.factorial(num))


# Input function to get the number from user
num = int(input('Please enter a number to find the factorial: '))

#Printing the factorial of the given number
print("The factorial of the given number", num, "is",
	factorial(num))

#-----------------------Write a Python code to calculate the square root of a given number.-----------

# Input function to get the input from the user
n = float(input('Enter a number: '))

#Formula to calculate the square root of the number
n_sqrt = n ** 0.5

#Printing the calculated square root of the given number
print('The square root of {0} is {1}'.format(n ,n_sqrt))

#--------------Write a Python code to calculate the area of a triangle.--------------


# Get the 3 sides of a triangle from the user
s1 = float(input('Enter first side value: '))
s2 = float(input('Enter second side value:'))
s3 = float(input('Enter third-side value:'))

#Calculating the semi-perimeter of a triangle
sp = (s1 + s2 + s3) / 2

#Calculating the area of a triangle
area = (sp*(sp-s1)*(sp-2)*(sp-s3)) ** 0.5

#Printing the area of the triangle
print('The area of the triangle is: ', area)

#------------------Write a Python code to check the armstrong number.-------------------

#Taking the input from user to check armstrong number
num=int(input("Enter the number to check armstrong number: "))

#Assigning the num value to arms
arms = num

#Finding the length of the number
length = len(str(num))
sum1 = 0

#Iterating the values to check armstrong number
while num != 0:
	rem = num % 10
	sum1 = sum1+(rem**length)
	num = num//10

#Printing the result whether the given number is armstrong number or not
if arms == sum1:
	print("The given number", arms, "is armstrong number")
else:
	print("The given number", arms, "is not an armstrong number")
    
#----------------Write a Python program to check leap year.-------------

# Function implementation to check leap year  
def LeapYear(Year):  
  #Condition to check if the given year is leap year or not  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("The given Year is a leap year");  
  # Else it is not a leap year  
  else:  
    print ("The given Year is not a leap year")  
# Taking an input year from user  
Year = int(input("Enter the year to check whether a leap year or not: "))  
# Printing the leap year result  
LeapYear(Year) 

#---------------Write a Python code to display a multiplication table using for loop.---------

#Get the number from the user for multipication table
tab_number = int(input ("Enter the number of your choice to print the multiplication table: "))      

#For loop to iterate the multiplication 10 times and print the table   
print ("The Multiplication Table of: ", tab_number)    
for count in range(1, 11):      
   print (tab_number, 'x', count, '=', tab_number * count)
   
#-----------Write a Python program to swap two variables.-----------------

# Take inputs from the user to swap the two variables
num1 = input('Enter the first variable: ')
num2 = input('Enter the second variable: ')

#Printing the numbers before swap
print('The value of num1 before swapping: {}'.format(num1))
print('The value of num2 before swapping: {}'.format(num2))

#Use temporary variable and swap the values
temp = num1
num1 = num2
num2 = temp

#Printing the numbers after swap
print('The value of num1 after swapping: {}'.format(num1))
print('The value of num2 after swapping: {}'.format(num2))

