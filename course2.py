# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:27:35 2019

@author: chniranjanreddy
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#read excel file
df = pd.read_excel ("population_total (1).xlsx",0) #read excel
#
#test=df[df.]
#
#df['column'].hist()
#totPop=df.sum(axis = 0, skipna = True)
##df.sum(axis = 1, skipna = True) 
#
#
#collsts = df.columns
#index1 = 0
#index = 1
#totpop = ([1]*(len(collsts)-2))
#while index < len(collsts)-1:
#    tmp = sum(df[collsts[index]])    
#    totpop[index1] = tmp/(10**9)
#    index = index+1
#    index1 = index1+1
##creation of an array using np lib
#years = np.arange(1800,2100,1) 
##matplotlib
#plt.plot(years, totpop,'r--')   
#plt.xlabel("years",fontsize=12,fontweight="bold")
#plt.ylabel("population in billions",fontsize=12,fontweight="bold")
#plt.xticks(fontsize=11,fontweight="bold")
#
#plt.yticks(fontsize=11,fontweight="bold")
#
#plt.savefig("myfirstfig.pdf")
#
#
#            