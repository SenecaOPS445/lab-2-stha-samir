#!/usr/bin/env python3

import sys  # Import sys to access command-line arguments

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
