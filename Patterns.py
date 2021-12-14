# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:25:34 2021

@author: Singh
"""
#-------------------------Patterns-----------------------

#Ex 1.
print("* * * *")
print("*")

#Ex 2.
print("* * * *")
print("* * * *")
print("* * * *")
print("* * * *")

#Ex 3.
for i in range(4):
    print("*")
    
#Ex 4.
for i in range(4):
    print("*",end=" ")
    
#Ex 5.
for i in range(4):
    print("*",end=" ")
print() # just to add a newline and it is executed after the complete excution of
for i in range(4):
    print("*",end=" ")
print()
for i in range(4):
    print("*",end=" ")
print()
for i in range(4):
    print("*",end=" ")
print()

#Ex 6.
for value in range(4):
    for i in range(4):
        print("*",end=" ")
    print()
    
#Ex 7. 
for col in range(6):
    print("*",end=" ")
print()
for col in range(6):
    print("*",end=" ")
print()
for col in range(6):
    print("*",end=" ")
print()
for col in range(6):
    print("*",end=" ")
print()

#Ex 8.
for row in range(3):
    for col in range(6):
        print("*",end=" ")
    print()
    
#Ex 9.
for row in range(5):  #row = 4
    for col in range(0,row+1): #col=range(0,5) => column can take value 0
        print("*",end=" ")
    print()

#Ex 10.
length = int(input()) 
for row in range(length):    
    for col in range(length - row):        
        print("*", end =' ')    
    print()

#Ex 11. 
no_of_row = int(input()) 
for row in range(no_of_row):    
    for col in range(no_of_row):        
        if(row+col>= no_of_row-1):            
            print("*", end = ' ')        
        else:            
                print(" ", end =' ')    
    print()
    
#Ex 12. 
for row in range(6):    
    for col in range(6):        
        if(col>=row):            
            print("*", end =' ')        
        else:            
            print(" ", end =' ')    
    print()

#Ex 13. 
for row in range(1,5):    
    for col in range(1,row+1):        
        print(col, end =" ")    
    print()

#Ex 14. 
for row in range(4):    
    for col in range(1,row+2):        
        print(col, end =" ")    
    print()
    
#Ex 15. 
for row in range(1,5):    
    for col in range(1,row+1):        
        print(row, end=' ')    
    print()

#Ex 16.
for row in range(4):    
    for col in range(1,row+2):        
        print(row+1, end=' ')    
    print()

#Ex 17. 
N = int(input()) 
for row in range(N):    
    for col in range(1, N-row+1):        
        print(col, end =" ")    
    print()
    
#Ex 18. 
N = int(input()) 
for row in range(0,N):    
    for col in range(0,N):        
        if(col>=row):            
            num = N - col      #extra value to take care of the current value in             
            print(num,end =" ")        
        else:            
            print(" ",end=" ")    
    print()

#Ex 19. 
#The base structure of the above pattern 
N = int(input()) 
for row in range(0,N):    
    for col in range(0,N):        
        num = N - col        
        print(num,end =" ")    
    print()
    
#Ex 20.
N = int(input()) 
for row in range(0,N):    
    for col in range(0,N):        
        if(col>=row):            
            print(N-col,end =" ")  #print statement can evaluate        
        else:            
            print(" ",end=" ")    
    print()

#Ex 21.
for row in range(0,4):    
    for col in range (0,row+1):        
        num = row + col + 1        
        print(num,end=" ")    
    print()

#Ex 22.
for row in range(1,5):     
    for col in range (row,row*2):          
        print(col,end=" ")    
    print()