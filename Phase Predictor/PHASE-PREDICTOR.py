#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import KFold 
import pandas as pd


# In[2]:


from sklearn import preprocessing
d1 = pd.read_csv("data.csv")
d2=d1['phase']
d3=d1.drop(['phase'], axis=1)
d= preprocessing.normalize(d3,axis=0)
df = pd.DataFrame(d)
df.insert(0, 'phase', d2)
train, test = train_test_split(df, test_size = 0.2, random_state = 1)


# In[3]:


def phase_predictor(vec,diffn,diffr,mixingh,mixinge):
    
    uniqueValues = train['phase'].unique()
    grouped = train.groupby(train.phase)
    SS_grp  = grouped.get_group("SS")
    AM_grp  = grouped.get_group("AM")
    IM_grp  = grouped.get_group("IM")
    distance=[]
    distance_1 = []
    
    distance.append(((vec-SS_grp[0].mean())**2+(diffn-SS_grp[1].mean())**2+(diffr-SS_grp[2].mean())**2+(mixingh-SS_grp[3].mean())**2+(mixinge-SS_grp[4].mean())**2)**0.5)
    distance.append(((vec-AM_grp[0].mean())**2+(diffn-AM_grp[1].mean())**2+(diffr-AM_grp[2].mean())**2+(mixingh-AM_grp[3].mean())**2+(mixinge-AM_grp[4].mean())**2)**0.5)
    distance.append(((vec-IM_grp[0].mean())**2+(diffn-IM_grp[1].mean())**2+(diffr-IM_grp[2].mean())**2+(mixingh-IM_grp[3].mean())**2+(mixinge-IM_grp[4].mean())**2)**0.5)
    
    distance_1 = [x for x in distance if ~np.isnan(x)]
    
    key = min(distance_1)
    for i in range(0,3):
        if key == distance[i]:
             a = i
   # print(distance_1)
    
    if (a == 0):
        a1="SS"
        return(a1)
    elif(a == 1):
        a2="AM"
        return(a2)
    elif(a == 2):
        a3="IM"
        return(a3)


# In[4]:


import tkinter as tk 
from functools import partial 
r = tk.Tk() 
r.title('Phase Predictor') 
myLabel = tk.Label(r,text="Phase Predictor",font=("Times New Roman", 35)) 
r.geometry("400x250")  
def interface_function(label_result,n1, n2, n3, n4, n5):
    num1=float(n1.get())
    num2=float(n2.get())
    num3=float(n3.get())
    num4=float(n4.get())
    num5=float(n5.get())
    result = phase_predictor(num1,num2,num3,num4,num5)
    label_result.config(text="Predicted Phase = %s" %result)  
    return  
    
number1 = tk.StringVar()  
number2 = tk.StringVar()  
number3 = tk.StringVar()  
number4 = tk.StringVar()    
number5 = tk.StringVar()  

vec = tk.Label(r, text = "Valence Electron Concentration").place(x = 650,y = 300)  
diffn = tk.Label(r, text = "Pauling Negativities Difference").place(x = 650, y = 340)  
diffr = tk.Label(r, text = "Atomic size difference").place(x = 650, y = 380) 
mixingh=tk.Label(r, text = "Mixing Entropy ").place(x = 650, y = 420)
mixinge=tk.Label(r, text = "Mixing Enthalpy").place(x = 650, y = 460)
labelResult = tk.Label(r)
labelResult.place(x = 700 , y = 550)  
e1 = tk.Entry(r , textvariable=number1).place(x = 830, y = 300) 
e2 = tk.Entry(r , textvariable=number2).place(x = 830, y = 340)  
e3 = tk.Entry(r , textvariable=number3).place(x =830 , y = 380)  
e4 = tk.Entry(r , textvariable=number4).place(x = 830, y = 420)
e5 = tk.Entry(r , textvariable=number5).place(x = 830, y = 460)
interface_function = partial(interface_function,labelResult, number1, number2, number3, number4, number5) 
button = tk.Button(r, text='Submit',command=interface_function).place(x=920,y=500) 
myLabel.pack( )
r.mainloop()

