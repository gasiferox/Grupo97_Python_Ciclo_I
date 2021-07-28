import math as m

dev = 0
mean = float
h = int
sum = 0
dev_1 = 0
diffe = 0

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

for i in players:
    sum += i

mean = sum / len(players)

for i in players:
    dev_1 += (i - mean) ** 2

dev = m.sqrt(dev_1/len(players))

devPlus = mean + dev
devMinus = mean - dev

for i in players:
    if i >= devMinus and i <= devPlus:
        diffe += 1

print(dev_1)
print(dev)
print(len(players))
print(devMinus)
print(devPlus)
print(diffe)
