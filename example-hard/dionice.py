days = int(input())
buy, sell, cash, current = [], [], [], 0
bought, sold = buy.append, sell.append
for _ in range(days):
    day = input()
    price = int(day[2])
    if day[0] == "2":
        bought(price)
        sold(0)
    else:
        bought(0)
        sold(price)

best = 0
for x in range(days):
    if sell[x] != 0:
        temp = [x for x in buy[best:x + 1] if x]
        best = x
        try:
            if sell[x] - min(temp) > 0:
                current += sell[x] - min(temp)
        except ValueError:
            continue

print(current)
