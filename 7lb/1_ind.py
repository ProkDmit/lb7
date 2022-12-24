#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input("Введите 10 элементов\n").split()))
    if len(A) != 10:
        print("Неверный размер массива", file=sys.stderr)
        exit(1)

    if min(A) < 0:
        pr = 0
        for i in range(len(A)):
            if A[i] < 0:
                pr += A[i]
        print(pr)
    else:
        print(0)
