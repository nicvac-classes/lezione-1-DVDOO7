#!/usr/bin/env python3

import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

sys.stdin = open('pile_input01.txt')
sys.stdout = open('output.txt', 'w')

def solve(t):
    input()

    N = int(input().strip())

    A = [0] * N
    B = [0] * N
    C = [0] * N

    for i in range(N):
        A[i], B[i], C[i] = map(int, input().strip().split())
    

    # aggiungi codice...

    max(A[i], B[i], C[i])

    risposta = 42


    print(f"Case #{t}: {risposta}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
