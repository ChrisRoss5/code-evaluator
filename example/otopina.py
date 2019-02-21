#!/usr/bin/python3

N = int(input())
volume = [int(x) for x in input().split()]
current = [int(x) for x in input().split()]


def check():
    for k in y:
        temp = current.copy()
        temp[k] += x
        temp[n - 1] = 0
        if temp[k] > volume[k]:
            remainder = temp[k] - volume[k]
            temp[n - 1] += remainder
            temp[k] -= remainder
        if N in temp:
            return str(n) + " " + str(k+1)


for n, x, y in zip(range(1, 4), current, ((1, 2), (0, 2), (0, 1))):
    result = check()
    if result is not None:
        print(result)
        break
else:
    print("0")
