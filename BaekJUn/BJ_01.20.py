# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:47:44 2022

@author: user
"""
#%% problem 10950
#How to solve problem about empty value?
T = range(1,3)

for i in T:
    A, B = map(int, input().split())
    try:
        if isinstance(A,int) & isinstance(B,int) == True:
            print(A+B)
        else:
            pass
    except:
        pass
#%% Final code 
T = int(input())

for i in range(1,T+1):
    try :
        A, B = map(int, input().split())
        print(A+B)
    except:
        pass

#%%
n = int(input())
a = 0
for i in range(n+1):
    a = a+i
    
print(a)

#%%
n = int(input())
a = sum(range(n+1))
print(a)