#!/usr/bin/env python3

import random
import math

fout = open("params", "w")

l = []

for i in range(1000):
	l.append(2**random.uniform(2, math.log(10**10, 2)))

l.sort()
l = [math.ceil(x) for x in l]

for i in l:
	fout.write("{} {}\n".format(i, random.randint(i, i**2)))

fout.close()
