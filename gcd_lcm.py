#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:22:44 2022

@author: suvankar
"""

import numpy as np

class lcm:
    def LCM(self, a, b):
        print(np.lcm(a,b))

class gcd:
    def GCD(self, a, b):
        print(np.gcd(a,b))


print("1.LCM\n2.GCD\n")

ch = int(input("Enter your choice : "))

a = int(input("Enter A: "))
b = int(input("Enter B : "))

if ch == 1:
    l = lcm()
    l.LCM(a, b)
if ch == 2:
    h = gcd()
    h.GCD(a, b)


