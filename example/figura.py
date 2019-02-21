from collections import deque
R, S = map(int, input().split())
matrix = [list(input()) for x in range(R)]
left = matrix[0].index("#")
right = matrix[0][::-1].index("#")
drops = dict()

for x in range(-left, right + 1):
    temp = []
    for i in range(S):
        if "#" not in matrix[i]:
            temp = list(map(list, zip(*(temp + matrix[i:]))))[::-1]
            break
        q = deque(matrix[i])
        q.rotate(x)
        temp.append(q)

    empty = 0
    drop = min(x.count(".") for x in temp)
    for i in range(S):
        height = temp[i].index(".")
        if not height:
            continue
        rest = temp[i][drop + height:]
        temp[i] = ["."] * drop + ["#"] * height + rest
        empty += rest.count(".")
    drops[empty] = list(zip(*temp[::-1]))

[print("".join(x)) for x in drops[min(drops)]]
# 8 5
# #####
# .###.
# ..#..
# .....
# .....
# ..#..
# .###.
# #####

# 7 7
# ..###..
# ..##...
# ..#....
# .......
# ......#
# ..#...#
# #######
