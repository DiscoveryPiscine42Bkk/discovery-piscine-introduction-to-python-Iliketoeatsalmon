#!/usr/bin/env python3
a = input("Enter the first number : ")
print(a)
b = input("Enter the Secound number : ")
print(b)
ans = int(a) * int(b)
#print(int(a + "x" + b + "=" + ans))

print(int(a) , "x" , int(b) , "=" , ans)

if ans > int(0):
    print("The result is positive.")
elif ans == int(0):
    print("The result is positive and negative.")
else:
    print("The result is Negative")