# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 23:39:36 2022

@author: sanha
"""

# 1271 엄청난 부자 

# m = 1000
# n = 3
m, n = map(int, input().split())

if bool(m % n) == True:
    least = m - (m % n)
    deviden = least // n # / 대신에 정수값을 반환해주는 //을 사용
    
    print(int(deviden))
    print(int(m - least))
else :
    deviden = m // n # / 대신에 정수값을 반환해주는 //을 사용
     
    print(int(deviden))
    print(int(m % n))

