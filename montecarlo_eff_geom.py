#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:14:33 2023

@author: tiziano
"""
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

import random as rnd
import math 


#FUNZIONER PER GENERARE GLI ANGOLI CASUALI

def randomtheta():
    while(True):
        x1=rnd.uniform(0,3.141/2)
        y1=rnd.uniform(0,10)
        if (y1<math.cos(x1)**2*math.sin(x1)):
            #print(x1)
            return x1
        #else:
            #print(x1,y1)
            #print("no")


# ---- PLOTTARE GLI ANGOLI PER VEDERE SE HA SENSO
N_points = 1000
n_bins = 20

# Generate two normal distributions
dist1 = []
for i in range(N_points):
    dist1.append(randomtheta())
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
axs[0].hist(dist1, bins=n_bins)



#---IL VERO CALCOLO MONTECARLO---
hit=0
nsim=100000
z=28.1
latox=36.5#30.3
latoy=30
lineax=[]
lineay=[]
lineax.append(-latox/2)
lineay.append(0)
lineax.append(latox/2)
lineay.append(0)
plt.xlim(-60,60)
plt.ylim(-60,z+40)
plt.plot(lineax,lineay,linewidth=3,color="b")

plt.plot([-latox/2,latox/2],[z,z],linewidth=4,color="b")
for i in range(nsim):
    x=rnd.uniform(-latox/2,latox/2)
    y=rnd.uniform(-latoy/2,latoy/2)
    phi=rnd.uniform(0,3.141)
    theta1=randomtheta()
    
    xS4=x-z*math.tan(theta1)*math.cos(phi)
    yS4=y-z*math.tan(theta1)*math.sin(phi)
    if ((abs(xS4)<latox/2) and (abs(yS4)<latoy/2)):
        hit=hit+1
    lineax=[]
    lineay=[]
    lineax.append(x)
    lineay.append(z)
    lineax.append(xS4)
    lineay.append(0)
    #plt.plot(lineax,lineay)
        

effgeom=hit/nsim




print(effgeom, " pm ", math.sqrt(hit)/nsim)


