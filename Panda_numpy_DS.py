#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:26:17 2022

@author: suvankar
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#s = pd.read_csv("/home/suvankar/python programs/PythonProgram2/csv files/bank_loan.csv")
#print(s['Balnc'].describe())
#print(s)

#print(s['Balnc'].mean())

#print(s['Balnc'].mode())

#print(s['Balnc'].max())

#print(s['Balnc'].min())

#print(s['Balnc']>500)

#print(s.head())

"""s.loc[s['Balnc'] > 60000 , 'Greter '] = 'Found'
print(s)

"""

#print(s[s['Balnc'] > 80000])

#matplotlib

data = pd.read_csv("/home/suvankar/python programs/PythonProgram2/csv files/bank_loan.csv")

print(data)

Balnc = data['Balnc']
data1 = data['Monthly_Credit']
actype = data['Act_type']

"""fig = plt.figure(figsize=(10, 7))
plt.pie(Balnc, labels = data1, autopct='%0.0f%%', shadow=True)
plt.show()"""

#plt.Figure()
plt.plot(Balnc, data1)
#plt.ion()
#plt.ylabel("Balance")
#plt.xlabel("Monthly Credit")
#plt.hist(data1)
plt.pie(data1, labels=data1)
plt.show()
