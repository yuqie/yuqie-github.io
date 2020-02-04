# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:02:44 2019

@author: qieyu
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def read_file(filename):
    fra_cathode = []
    fra_SSE = []
    E_total = []
    E_mutual = []
    i = 0
    
    f = open(filename,"r")  
    for line in f.readlines():
        i = i+1
        # skip the first line
        if i==1:
            continue
        if line.strip():
            a = line.strip().split()
            fra_cathode.append(float(a[2]))
            fra_SSE.append(float(a[3]))
            E_total.append(float(a[4]))
            E_mutual.append(float(a[5]))
            i=i+1
    #E_mutual.pop(3)  #delete Na2MnPO4F
    return E_mutual

mpl.rc('font',family='Times New Roman')
colorpalette = plt.cm.rainbow(np.linspace(0,1,6))

filename =  ['NYC_Minimum_reaction-with-old-NVPF.txt','NYB_Minimum_reaction-with-old-NVPF.txt','NPS_Minimum_reaction.csv','NGPS_138_Minimum_reaction.csv']
x_label = [i.split('_')[0] for i in filename]
s = ['NaCoO$_{2}$',"NaCrO$_2$","Na$_{2}$FePO$_{4}$F","Na$_{2}$MnPO$_{4}$F","Na$_{3}$V$_{2}$(PO$_{4}$)$_{3}$","Na$_{3}$V$_{2}$(PO$_{4}$)$_{2}$F$_3$"]

#read from file
x = [[],[],[],[]]
n_bins = len(filename)
for i in range(len(filename)):
  #  print(filename[i])
    E_mutual = read_file(filename[i])
  #  print(E_mutual)
    x[i] = E_mutual
x = np.array(x).T

fig, ax = plt.subplots(figsize=(7.5, 5))

# set width of bar
barWidth = 0.15

# Set position of bar on X axis
r1 = np.arange(len(x[0]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]  #delete Na2MnPO4F
r = [r1,r2,r3,r4,r5,r6]

# Make the plot
for i in range(5):#delete Na2MnPO4F
    # keep color compatibility
    j = i          
    if i>2:
        i=i+1
    plt.bar(r[j], x[i], color=colorpalette[i], width=barWidth, edgecolor='white', label=s[i])
    print(i)
# Add xticks on the middle of the group bars
#plt.xlabel('group', fontweight='bold',fontsize=20, fontname="Times New Roman")
plt.xticks([r + barWidth for r in range(len(x[1]))], x_label,fontsize=24, fontname="Times New Roman")
plt.ylabel('Reaction energy (meV/atom)', fontsize=24, fontname="Times New Roman")
plt.yticks(np.arange(0,-401,-100),fontsize=20, fontname="Times New Roman")

# reverse y-axis
ax = plt.gca()
ax.invert_yaxis()

# Create legend & Show graphic
plt.legend( loc='upper left', shadow=True, fontsize=20, ncol=1) #bbox_to_anchor=(x, y),

fig.tight_layout()
plt.savefig('RxnE_cathodes_SSEs_bar.png', dpi=300)#, bbox_inches='tight')

plt.show()



