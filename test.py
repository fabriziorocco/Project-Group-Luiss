#!/usr/bin/env python3
import sys
import os
import subprocess

for line in sys.stdin:
	N, V = line.split()
	os.system("./gen.o {} {} > output.txt".format(N, V))
	t = subprocess.check_output('/usr/bin/time -f "%e" ./sol.o 2>&1', shell=True)
	t = float(t)
	print("{} {} {}".format(N, V, t))
