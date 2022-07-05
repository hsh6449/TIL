# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 09:58:10 2022

@author: user
"""
#%% 15552 A+B 출력하기(만약 오류가 날경우 계산 없이 넘어가는 코드로 작성)
import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    try :
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        pass
#%% 2741
import sys
N = int(sys.stdin.readline())

for i in range(1,N+1):
    print(i)
#%% 2742
import sys
N = int(sys.stdin.readline())

for i in range(N) :
    print(N-i)

#%% 11021 format이용하기

T = int(input())

for i in range(1,T+1):
    try :
        A, B = map(int, input().split())
        print(f'Case #{i}:',A+B)
    except:
        pass
    
#%% 11022 format을 이용해서 출력하기

T = int(input())

for i in range(1,T+1):
    try :
        A, B = map(int, input().split())
        print(f'Case #{i}: {A} + {B} =',A+B)
    except:
        pass
    
#%% 2438 별 찍기

N = int(input())

for i in range(1,N+1):
    print('*' * i) #str에 숫자를 곱하면 그 수만큼 출력됨
    
#%% 2439 별 반대로 찍기

N = int(input())

for i in range(1,N+1):
    print(' ' * (N - i) + '*' * i) #빈칸을 N-i만큼 먼저 출력해주고 별의 개수를 출력

    
    
