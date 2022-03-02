#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:05:21 2022

@author: suvankar
"""

#Write a C program to find the sum of the following series: 
#1+11+111+1111+.... upto N terms

n = int(input("Enter no of terms : "))

a = 1
sum=0
for i in range(1,n+1):
    sum = sum+a
    a=a*10+1

print(sum)
    