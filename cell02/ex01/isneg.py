#!/usr/bin/env python3
number = input()
if number.strip() < "0":
    print("This number is Negative")
elif number.strip() == "0":
    print("TThis number is both positive and negative.")
else:
    print("This number is Positive")
