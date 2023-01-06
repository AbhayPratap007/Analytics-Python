# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:02:50 2021

@author: Singh
"""
#abs(): Returns the absolute value of a number.
#  integer number     
integer = -20
abs(integer)  
print('Absolute value of -20 is:', abs(integer))  
  
#  floating number  
floating = -20.83  
print('Absolute value of -20.83 is:', abs(floating))  

#all(): It returns true if all items passed in iterable object are true. 
#Otherwise, it returns False.
#This fxn accepts an iterable object (such as list, dictionary, etc.). 
# all values true  
k = [1, 3, 4, 6]  
print(all(k))
  
# all values false  
k = [0, False]  
print(all(k))  
  
# one false value  
k = [1, 3, 7, 0]  
print(all(k))
  
# empty iterable  
k = []  
print(all(k)) 

#------------------------------------------------------------------------------------

#bool(): Converts a value to boolean(True or False)
test1 = []  
print(test1,'is',bool(test1)) 

test1 = [0]
print(test1,'is',bool(test1))    

test1 = None  
print(test1,'is',bool(test1))  

test1 = 'Easy string'  
print(test1,'is',bool(test1)) 

#sum(): Used to get the sum of numbers of an iterable, i.e., list.
list_1 = [1,2,4]  
s = sum(list_1)  
print(s)  
  
s = sum(list_1, 10)  
print(s) 

#Sum of all items without using sum function.
s=0
list=[1,2,3]
for i in list:
  s=s+i
 print(s)
#-------------------------------------------------------
import statistics
nums = [12,45,67,78]
ave=statistics.mean(nums)
print(ave)
#------------------------------------------------------

#Find Average
list=[44,56,-1,-6,-2,19, 15, 18, 12, 97, 12, -100, -5, 5,23]
tot=0
for i in list:
  tot=tot+i
Average = tot/len(list)
print(Average)

#len(): Returns the length (the number of items) of an object.
strA = 'Python'  
print(len(strA))  

#list() creates a list in python.
# empty list  
Gaurav = list()
print(Gaurav)  
  
#Converting string to list
String = 'abcde'       
print(list(String)) 

#divmod(): Used to get quotient and remainder of two numbers. 
#This function takes two numeric arguments and returns a tuple. 
#Both arguments are required and numeric 
# Calling function  
result = divmod(10,2)  
# Displaying result  
print(result)  

#dict(): Its a constructor which creates a dictionary. 
# Calling function  
result = dict() # returns an empty dictionary 
print(result)
 
result2 = dict(a=1,b=2)  
# Displaying result  
print(result2)  

#set(): It is used to create a new set using elements passed during the call. 
#It takes an iterable object as an argument and returns a new set object.
# Calling function  
result = set() # empty set  
result2 = set('12')  
result3 = set('javatpoint') 
result4 = {1,2}
print (result4)
# Displaying result  
print(result)  
print(result2)  
print(result3)  

#pow(): Used to compute the power of a number.
# positive x, positive y (x**y)  
print(pow(4, 2))  
  
# negative x, positive y  
print(pow(-4, 2))  

#tuple(): Used to create a tuple object.
t1 = tuple()  
print('t1=', t1)  
  
# creating a tuple from a list 
l =  [1, 6, 9]
t2 = tuple(l)  
print('t2=', t2)  
  
# creating a tuple from a string  
t1 = tuple('Java') 
print('t1=',t1)  

#----------------------------------------------------------------------
#lambda()- Helps creating anonymous functions. 
#Lambda functions can accept any number of arguments, 
#but they can return only one value in the form of expression.

#Multiple arguments to Lambda function
x = lambda a,b:a+b 
# a and b are the arguments and a+b is the expression which gets evaluated and returned.   
print("Addition = ",x(20,10)) 

#Program to filter out the list which contains numbers  divisible by 3.
List = [1,2,3,4,10,123,22]  
Oddlist = list(filter(lambda x:(x%3 == 0),List)) 
# the list contains all the items of the list for which the lambda function evaluates to true  
print(Oddlist) 

#program to triple each number of the list using map  
List = [1,2,3,4,10,123,22] 
new_list = list(map(lambda x:x*3,List)) 
# this will return the triple of each item of the list and add it to new_list  
print(new_list)  

#-------------------------def function()----------------
#Parameter – It is data or variable defined inside parenthesis – (). 
#Argument – It is the value of parameter.
#Creating a Function – In Python, a function is created by using def keyword.
#def – It is Python’s built-in function. It used to create a function in Python.

#def function
def my_function(x):
  return 5 * x
print (my_function(3))

#print hello
def func():
    print ('Hello Print')
func()

#creating Argument:- A argument is passed after the function name and inside the parentheses. An argument can be passed as many as want to pass. A function treated argument as value of parameter or an information into function.

def my_func(i):
     print(i)
my_func('Hello, Python World') 

def my_func(i):
     print(i + 5)
my_func(10)

#Number of Arguments – A function normally called by default number of arguments, means the number of argument which want to pass but if a function doesn’t call to its equal number of argument then Python will give us an error.
def my_func(x , y):
     print(x+y)
my_func(5) 
my_func(12) 

#Calling a function with its equal number of arguments.

def my_func(x , y):
     print(x+y)
my_func(5,10) 

#Arbitrary Arguments, *args – When it is not defined how many parameters should be passed, then add an asterisk (*) before the name of the parameter.  It will make sure function to receive the number of tuple argument according to its requirement.
def my_func(x):
     print(x[0])
my_func(5,10,15) 
#If the number of arguments is not defined, add an asterisk (*) before the parameter name.
def my_func(*x):
     print(x[0])
my_func(5,10,15) 

#Keyword Argument – An argument can be sent as key-value pair. In this way argument order doesn’t matter. In other words, a keyword is a value defined on the left-hand side and an argument is the value defined on the right-hand side followed by assignment statement (=)
def my_func(x,y):
     print('The sum of all argument is:' , x+y) 
my_func(y=5, x=10) 

#Arbitrary Keyword Arguments, **kwargs – If it is not defined that how many keyword arguments (kwargs) should be passed to a function then add two asterisks (**) before the parameter name. It will make sure function to receive the dictionary of arguments according to its need.
def my_func(**x):
     print('The number is', x['z'])
my_func(x = 5, y = 10, z = 15) 

#Default Parameter Value – When a function called without parameter then it takes default parameter.
# Calling a function with its default parameter.

def my_func(x = 'Alex'):
     print('My name is ' + x)
my_func() 

#Calling a function with both default parameter and additional key value pair.

def my_func(x = 'Alex'):
      print('My name is ' + x)
my_func('Elisa')
my_func()
my_func('Kily') 

#Passing data types as an Argument – An argument can receive any kind of data types such as list, tuple, set and dictionary etc. it will be treated as the same data type inside the function.

#Passed an argument of elements as tuple to function.
def my_func(n):
     for x in n:
         print(x)
z = (1,2,3,4)
my_func(z) 

#Return values – To let return a function its value use ‘return’ keyword.

def my_func(x):
     return 3 + x
print(my_func(4))
print(my_func(6)) 

#pass Statement – A function statement can not be empty, but in case it is necessary to leave empty then use pass keyword to leave a function statement empty.
#Use pass keyword to leave a function statement empty.

def my_func():
      pass
  
  #Recursion – It means when a defined function calls itself.
  #Calling a function to itself.
  
  def my_func(x):
     if x > 0:
         r = x + my_func(x-1)
         print(r)
     else:
         r = 0
     return r
 print( "\nRecursion Example Results" )
 my_func(8)
