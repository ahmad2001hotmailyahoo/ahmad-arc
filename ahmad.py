x = int(input("Enter the no. of value up to which you want to print series of 11\n"))
y = 0
add = 0
for i in range(x):
    y = y + pow(10, i)
    add = add + y
    print(y, " + ", end="")
print("\b\b\b", end="")
print(" = ", add)
 