#!/usr/bin/python3

n = int(input())
a, b = map(int, input().split())

ukupno = n * (n + 1) // 2
red = [0 for i in range(ukupno + 1)]
dijag1 = [0 for i in range(ukupno + 1)]
dijag2 = [0 for i in range(ukupno + 1)]

trenutni_red = 1
stupac = 0
for i in range(1, ukupno + 1):
    if stupac == trenutni_red:
        trenutni_red += 1
        stupac = 0
    red[i] = trenutni_red
    stupac += 1
    dijag1[i] = stupac
    dijag2[i] = trenutni_red - stupac + 1

for c in range(1, ukupno + 1):
    isti_red, ista_dijag1, ista_dijag2 = 0, 0, 0
    for i in (a, b, c):
        for j in (a, b, c):
            if i < j:
                isti_red += (red[i] == red[j])
                ista_dijag1 += (dijag1[i] == dijag1[j])
                ista_dijag2 += (dijag2[i] == dijag2[j])
    if isti_red == ista_dijag1 == ista_dijag2 == 1:
        print(c)
