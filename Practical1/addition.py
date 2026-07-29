num = int(input("Enter a number: "))

total = 0

for i in range(num, 0, -1):
    print(i, end="")

    total += i

    if i > 1:
        print(" + ", end="")

print(" =", total)