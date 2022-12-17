#!/usr/bin/env python3
#-*- coding: utf-8 -*-
if __name__=='__main__':
    A=list(map(int, input("Введите элементы:\n").split()))
    s1, s2, k1, k2=0, 0, 0, 0
    for i in range(len(A)):
        if i%2!=0:
            s1+=A[i]
        if A[i]<0:
            if k1==0:
                k1=i
            k2=i
    print("Сумма элементом с нечетными номерами:", s1)
    for i in range(len(A)):
        if i>k1 and i<k2:
            s2+=A[i]
    print("Сумма элементом между 1 и последним отрицательными элементами", s2)
    c=0
    for i in range(len(A)):
        if A[i]>1:
            del A[i]
            c+=1
    for i in range(c):
        A.append(0)
    print(A)