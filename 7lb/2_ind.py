#!/usr/bin/env python3
#-*- coding: utf-8 -*-
if __name__=='__main__':
    A=list(map(int, input("Введите целые элементы\n").split()))
    p, s, k1, k2=1, 0, 0, 0
    for i in range(len(A)):
        if i%2==0:
            p*=A[i]
        if A[i]==0:
            if k1==0:
                k1=i
            k2=i
    print("Произведение элементов списка с четными номерами:", p)
    for i in range(len(A)):
        if A[i]>k1 and A[i]<k2:
            s+=A[i]
    print("Сумма элементов между первым и последним 0 элементом:", s)
    so=sorted(list(filter(lambda x: x>=0, A)))+sorted(list(filter(lambda x: x<0, A)))
    print(so)