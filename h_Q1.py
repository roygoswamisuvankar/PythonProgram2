# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Write a C program to find the sum of the following series:
#2+5+8+11+14+ ........ upto N terms

n = int(input("Enter number of terms : "))

a = 2
sum = 0
for i in range(1,n+1):
    sum = sum + a
    a = a+3
    
print(sum)
        