# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:04:47 2019

@author: qieyu
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np
import math


def read_file(filename):
    fra_cathode = []
    fra_SSE = []
    E_total = []
    E_mutual = []
    flag =[]
    i = 0
    flag.append(i)
    
    f = open(filename,"r")  
    for line in f.readlines():
        if line.strip():
            a = line.strip().split()
            fra_cathode.append(float(a[1]))
            fra_SSE.append(float(a[2]))
            E_total.append(float(a[3]))
            E_mutual.append(float(a[4]))
            i=i+1
        else:
            flag.append(i)
    flag.append(i)
    return fra_SSE,E_mutual,flag


def plot_lines(flag,colorpalette,ax,filename,test_pos_y):
    for j in range(len(flag)-1):
        if j==3:
            continue
        x = []
        y = []
        for i in range(flag[j],flag[j+1]):
            x.append(fra_SSE[i])
            y.append(E_mutual[i])
            #print(x)
            #print(y)
            ax.plot(x,y,marker='*', color=colorpalette[j], linewidth=2, label=s[j]) # linestyle='dashed'    
            ax.axhline(y=0, color='k', linestyle='dashed')
            ax.set_xlabel("Molar fraction of %s in the pesudo-binary x" % filename.split('_')[0], fontsize=24, fontname="Times New Roman")
            ax.set_ylabel(r'Mutual Rxn. E. (meV/atom)', fontsize=24, fontname="Times New Roman")
            plt.xticks(fontsize=20, fontname="Times New Roman")
            plt.yticks(fontsize=20, fontname="Times New Roman")
    plt.text(0.8,test_pos_y,filename.split('_')[0],fontsize=24, fontname="Times New Roman")
    return
      

def legend_without_duplicate_labels(ax,fig): #,x,y):
    handles, labels = ax.get_legend_handles_labels()
    unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
    fig.legend(*zip(*unique), loc='upper center',bbox_to_anchor=(0.5, 0.28), shadow=True, fontsize=20, ncol=5)
    #

#filename =  ['NYC_full_evolution.csv','NYB_full_evolution.csv','NPS_full_evolution.csv']
filename =  ['NYC_full_evolution-with-old-NVPF.txt','NYB_full_evolution-with-old-NVPF.txt','NPS_full_evolution.csv','NGPS_138_full_evolution.csv'] #with old NVPF data  ps:old data smaller than the new data
#x_label = ['NYC','NYB','NPS']
s = ['NaCoO$_{2}$',"NaCrO$_2$","Na$_{2}$FePO$_{4}$F","Na$_{2}$MnPO$_{4}$F","Na$_{3}$V$_{2}$(PO$_{4}$)$_{3}$","Na$_{3}$V$_{2}$(PO$_{4}$)$_{2}$F$_3$"]
colorpalette = plt.cm.rainbow(np.linspace(0,1,6))
mpl.rc('font',family='Times New Roman') #used to set a single default font

N = len(filename)+1
cols = 2
rows = int(math.ceil(N / cols))

gs = gridspec.GridSpec(rows, cols)

fig = plt.figure(figsize=(15, 5*rows))

test_pos_y = [-100,-100,-325,-275]

for i in range(len(filename)):
    fra_SSE = []
    E_mtual = []
    flag =[]
    fra_SSE, E_mutual, flag = read_file(filename[i])
    #print(flag)
    #plt.subplots_adjust( wspace=0.2, hspace=0.2)
    ax = fig.add_subplot(gs[i])
    #ax = plt.subplot(len(filename)//2+1,2,i)  # python3 division always returns a float, usr floor() or //
    plot_lines(flag,colorpalette,ax,filename[i],test_pos_y[i])

loc_x = 0.85
loc_y = 1/rows*0.3
legend_without_duplicate_labels(ax,fig)#,loc_x,loc_y)
#handles, labels = ax.get_legend_handles_labels()
#fig.legend(handles, labels, loc='upper center')

#plt.legend(fontsize=20)
fig.tight_layout()
plt.savefig('RxnE_cathodes_SSEs.png', dpi=300)#, bbox_inches='tight')

plt.show()