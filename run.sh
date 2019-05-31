#!/bin/bash

echo "Compiling..."
g++ ./gen.cpp -Ofast -o ./gen.o
g++ ./sol.cpp -Ofast -o ./sol.o

echo "Generating parameters..."
python3 genParams.py

echo "Testing..."
python3 test.py < params > res
echo "Done!"
echo 'Run "cat res" to view test results'

python3 showRes.py
