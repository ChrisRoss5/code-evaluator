n = int(input())
a, b = sorted(map(int, input().split()))
pyramid = []
coords_a, coords_b = [], []
result = []

i = 1
for row in range(1, n + 1):
    temp = []
    for block in range(row):
        if i == a:
            coords_a = [row - 1, block]
        elif i == b:
            coords_b = [row - 1, block]
        temp.append(i)
        i += 1
    pyramid.append(temp)


def diagonal(side, direction):
    if a in side and b in side:
        distance = side.index(b) - side.index(a)
        if direction:
            cx1, cy1 = [coords_a[0], coords_a[1] - distance]
            cx2, cy2 = [coords_b[0], coords_b[1] + distance]
            if cy1 > -1:
                result.append(pyramid[cx1][cy1])
        else:
            cx1, cy1 = [coords_a[0], coords_a[1] + distance]
            cx2, cy2 = [coords_b[0], coords_b[1] - distance]
            if cy1 < len(pyramid[cx1]):
                result.append(pyramid[cx1][cy1])

        result.append(pyramid[cx2][cy2])
        return True


if coords_a[0] == coords_b[0]:  # same i
    result.append(pyramid[coords_a[0] - (b - a)][coords_a[1]])  # up
    x, y = coords_a[0] + (b - a), coords_a[1] + (b - a)  # down
    if x < n:
        result.append(pyramid[x][y])
else:
    left = [pyramid[x][coords_a[1]] for x in range(coords_a[0], n)
            if len(pyramid[x]) > coords_a[1]]
    right = [pyramid[x][y] for x, y in
             zip(range(coords_a[0], n), range(coords_a[1], n))]

    if not diagonal(left, 1):  # left
        diagonal(right, 0)  # right


print("\n".join(map(str, sorted(result))))
