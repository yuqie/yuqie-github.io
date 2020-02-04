# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:18:06 2019

@author: qieyu
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

label_num = []
labels = []
low_val = []
high_val = []
RxnE = []
flag =[]
i = 0
flag.append(i)
s = ["Fluorides","Chlorides","Bromides","Iodides","Oxides","Sulfides"]

f = open("NVPF_sorted.dat","r")
for line in f.readlines():
    if line.strip():
        a = line.strip().split()
        #label_num.append(a[0])
        label_num.append(int(i)+0.5)
        labels.append(a[2])
        low_val.append(-1*float(a[3]))
        high_val.append(-1*float(a[4]))
        RxnE.append(a[4])
        i=i+1
    else:
        flag.append(i)
        #i=i+1
flag.append(i)
#print(flag)

#label_num = np.asarray(label_num)
#labels = np.asarray(labels)
#low_val = np.asarray(low_val)
#high_val = np.asarray(high_val)
#RxnE = np.asarray(RxnE)

#colorpalette = np.asarray(['bule','red','olive','magenta','yellow','cyan'])
colorpalette=plt.cm.rainbow(np.linspace(0,1,6))

#fig = plt.figure(figsize=(15, 8))
fig, ax = plt.subplots(figsize=(15, 8.5))
#fig = plt.figure(figsize=(15, 8))
#ax = fig.add_subplot()

for j in range(len(flag)-1):
    #print(j,flag[j])
    C=colorpalette[j]
    #print(C)
    for i in range(flag[j],flag[j+1]):
        ax.fill_between([i,i+1],low_val[i],high_val[i],fc=colorpalette[j],edgecolor="black")
    #add legend  
    ax.fill_between([30,33],7.5-float(j)*0.55,7.0-float(j)*0.55,fc=colorpalette[j],edgecolor="black")
    #add text
    plt.text(34, 7.1-float(j)*0.55 , s[j], fontsize=24, fontname="Times New Roman")
    
    
ax.set_ylabel(r'Volage vs Na/$\rm Na^{+} $ (V)', fontsize=24, fontname="Times New Roman")
plt.yticks(fontsize=20, fontname="Times New Roman")
ax.set_xticks(np.asarray(label_num))
ax.set_xticklabels(labels,rotation='vertical', fontsize=20, fontname="Times New Roman")
#ax.legend()
plt.savefig('windows_Na_SSEs.png', dpi=300, bbox_inches='tight')
