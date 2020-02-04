# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:57:18 2020
Usage: convert *car to VASP POSCAR
       
01/24/2020
@author: qieyu
"""
import numpy as np
from numpy import pi, cos, sin, sqrt, dot

input_fname = "5_5.car"
output_fname = "5_5.vasp"
sys_name = output_fname

e_name = []
e_num=[]
x = []
y = []
z = []

# read from car file
f = open(input_fname,"r")
lines = f.readlines()
f.close()

for line in lines:
    tmp = line.split()
    if len(tmp) == 8:
        a = float(tmp[1])
        b = float(tmp[2])
        c = float(tmp[3])
        alpha = float(tmp[4])/180*pi  
        beta = float(tmp[5])/180*pi
        gamma = float(tmp[6])/180*pi
    if len(tmp) == 9:
       x.append(float(tmp[1]))  
       y.append(float(tmp[2]))
       z.append(float(tmp[3]))
     #  print(tmp[7])
       if tmp[7] in e_name:
           e_num[-1] = e_num[-1]+1
       else:
           e_name.append(tmp[7])
           e_num.append(1) 

# convert cell parameter line in car to a cell parameter matrix 
# set a is along the direction of X, b is on the XY plane, Z is along the normal direction of ab_plane, then
# dot(a,c)=a*c*cos(beta)
# dot(b,c)=b*c*cos(alpha)
# c**2 = c1**2+c2**2+c3**2
 
A = [a,0,0]
B = [b*cos(gamma),b*sin(gamma),0]
C = [c*cos(beta),(b*c*cos(alpha)-c*cos(beta)*b*cos(gamma))/b ,sqrt(c**2-(c*cos(beta))**2-((b*c*cos(alpha)-c*cos(beta)*b*cos(gamma))/b)**2)]
A = [np.round(i,8) for i in A]
B = [np.round(i,8) for i in B]
C = [np.round(i,8) for i in C]
Cell = [A,B,C]
#print(Cell)
old_pos = [x,y,z]
"""
# new position = Cell*(x,y,z)
Cell_new = np.array([[i/a for i in A],[i/b for i in B],[i/c for i in C]])
#print(Cell_new)
new_pos = dot(Cell_new,old_pos)
#print(new_pos)
"""
new_pos=old_pos
# write to VASP POSCAR file
fw = open(output_fname,"w+")
fw.write(" %s \n" % sys_name)
fw.write(" 1.0 \n" )
for i in range(3):
     fw.write( "%10.9f %10.9f %10.9f  \n "% (Cell[i][0], Cell[i][1], Cell[i][2])) 
for i in range(len(e_name)):
    if i==len(e_name)-1:
        fw.write("%5s \n" %e_name[i])
    else:                    
        fw.write("%5s " %e_name[i])
for i in range(len(e_num)):
    if i==len(e_num)-1:
        fw.write("%5d \n" %e_num[i])
    else:                    
        fw.write("%5d " %e_num[i])    
fw.write("Cartesian \n" )
for i in range(len(x)):
    fw.write( " %10.9f %10.9f %10.9f  \n "% (new_pos[0][i], new_pos[1][i], new_pos[2][i]))    # how to align left
fw.close()  
