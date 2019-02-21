N = int(input())
matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    matrix[i][1:] = list(map(int, input().split()))
matrix2 = matrix[:]
result = []


for i in range(1, N + 1):
    Sum = 0
    for j in range(1, N + 1):
        Sum += matrix[i][j]
        matrix2[i][j] = matrix[i - 1][j] + Sum

append = result.append
for rep in range(2):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            r1, r2, c1, c2 = i, i + rep, j, j + rep
            if r2 > N or c2 > N:
                continue
            temp = matrix2[r2][c2] - matrix2[r1 - 1][c2] \
                - matrix2[r2][c1 - 1] + matrix2[r1 - 1][c1 - 1]
            append(temp)
            while r1 > 1 and r2 < N and c1 > 1 and c2 < N:
                r1 -= 1
                r2 += 1
                c1 -= 1
                c2 += 1
                temp += matrix2[r2][c2] - matrix2[r1 - 1][c2] \
                    - matrix2[r2][c1 - 1] + matrix2[r1 - 1][c1 - 1]
                append(temp)

print(max(result))


# def factorize(field):
#     total, factor = 0, 1
#     while field:
#         for side in range(4):
#             if field:
#                 total += sum(field.pop(0)) * factor
#                 field = list(zip(*field))[::-1]
#         factor += 1
#     return total
#
#
# fertility = []
# for n in range(1, N - 1):
#     for i in range(N - n):
#         for j in range(N - n):
#             f = factorize([matrix[i + k][j:j + n + 1] for k in range(n + 1)])
#             fertility.append(f)
#
# print(max(fertility))
