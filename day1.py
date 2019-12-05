#!/usr/bin/python3

f = open("input.day1", "rt")

lines = f.readlines();
numbers = (int(i) for i in lines)

results = (i // 3 - 2 for i in numbers)

print("result is %s" % sum(results))
