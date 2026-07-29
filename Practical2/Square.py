# Input from the user
n = int(input("Enter the value of n: "))

# Print powers of 2 from 2^0 to 2^n
for i in range(n + 1):
    print(2 ** i)