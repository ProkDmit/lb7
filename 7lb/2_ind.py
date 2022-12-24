#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    A = list(map(int, input("Введите оценки по алгебре\n").split()))
    G = list(map(int, input("Введите оценки по геометрии\n").split()))
    F = list(map(int, input("Введите оценки по физике\n").split()))

    a = g = f = 0
    for i in range(len(A)):
        if A[i] > G[i] and A[i] > F[i]:
            a += 1
        if G[i] > A[i] and G[i] > F[i]:
            g += 1
        if F[i] > A[i] and F[i] > G[i]:
            f += 1

    print("Кол-во оценок по алгебре лучше:", a)
    print("Кол-во оценок по геометрии лучше:", g)
    print("Кол-во оценок по физике лучше:", f)

    if a > g and a > f:
        print("Лучшие оценки по алгебре")
    if g > a and g > f:
        print("Лучшие оценки по геометри")
    if f > a and f > g:
        print("Лучшие оценки по физике")
