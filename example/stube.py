#!/usr/bin/python3

N = int(input())
stairs = list(map(int, input().split()))

right = len(stairs)-1
result = []

for x in range(N):
    temp = stairs.copy()
    total_added = 0
    for y in range(right - 1):
        if temp[y + 1] <= temp[y]:
            add = temp[y] - temp[y + 1] + 1
            total_added += add
            temp[y + 1] += add
    for z in range(len(temp) - 1, right - 1, -1):
        if temp[z - 1] <= temp[z]:
            add = temp[z] - temp[z - 1] + 1
            total_added += add
            temp[z - 1] += add
    result.append(total_added)
    right -= 1

print(str(min(result)))
