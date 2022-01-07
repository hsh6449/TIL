# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:45:36 2022

@author: user
"""

#%% baekjun 14681
a, b = int(input()), int(input())

if (a>0)&(b>0):
    print(1)
elif (a<0)&(b>0):
    print(2)
elif (a<0)&(b<0) :
    print(3)
else :
    print(4)
    
#%% 
H, M = map(int, input().split(' '))


if (0<=M<45)&(H>0) : 
    print(H-1,M+15)
elif (M >= 45)&(H>0) : 
    print(H,M-45)
elif (0<= M <45)&(H == 0):
    print(H+23,M+15)
else :
    print(H,M-45)
#%% 2739
N = int(input())
for i in range(1,10):
    print(f'{N} * {i} = {N*i}' )