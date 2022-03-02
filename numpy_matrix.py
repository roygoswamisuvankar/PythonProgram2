#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:50:30 2022

@author: suvankar
"""

import numpy as np
from numpy import *

m = int(input("Enter row number : "))
n = int(input("Enter coloumn number : "))

#initialization array
a = zeros((m,n), dtype=int)

for i in range(len(a)):
    for j in range(len(a[i])):
        x = int(input())
        
        a[i][j] = x
        

print("The matrix is : \n")
print(a)
print("\n")
print(a.transpose())
    


