#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = list(map(int, input("Введите оценки по алгебре\n").split()))
    G = list(map(int, input("Введите оценки по геометрии\n").split()))
    F = list(map(int, input("Введите оценки по физике\n").split()))

    a = g = f = 0
    for i, item in enumerate(A):
        if item > G[i] and item > F[i]:
            a += 1
        if G[i] > item and G[i] > F[i]:
            g += 1
        if F[i] > item and F[i] > G[i]:
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
