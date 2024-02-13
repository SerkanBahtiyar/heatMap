# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:30:16 2024

@author: serkan
"""
#heatmap
import seaborn as sns
flights=sns.load_dataset('flights')
df=flights.copy()
df.head
df.shape
df["passengers"].describe()
df=df.pivot("month","year","passengers") #x,y,surekliDegisken
df
sns.heatmap(df)
sns.heatmap(df, annot=True, fmt="d", linewidths=.5);


#iki degisken arasi dogrusal iliski
import seaborn as sns
import matplotlib.pyplot as plt 
tips=sns.load_dataset("tips")
df=tips.copy()
df.head
sns.lmplot(x="total_bill",y="tip",data=df);
sns.lmplot(x="total_bill",y="tip", hue="smoker",data=df);
sns.lmplot(x="total_bill",y="tip", hue="smoker",col="time",data=df);
sns.lmplot(x="total_bill",y="tip", hue="smoker",col="time", row="sex",data=df);