#!/usr/bin/python3


f = open("input.day1", "rt")

lines = f.readlines();
numbers = (int(i) for i in lines)

results = []

for i in numbers:
    res = i // 2 - 2
    while i // 2 - 2 > 0:
        i = i // 2 - 2
        res += i
    results.append(res)

print(sum(results))
