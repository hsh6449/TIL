# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 00:25:02 2022

@author: user
"""
#%%

# 2339 긴자리 계산

a,b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)

#%%

# 2420 사파리 월드 (두 수 비교)

m,n = map(int, input().split())

dif = abs(n - m)

print(dif)

#%% 

# 2475 검증수

a = list(map(int, input().split()))

sum = 0
for i in a:
    sum = sum+i**2
print(sum % 10)