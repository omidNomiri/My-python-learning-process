x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

gcd_number = x
lcm_number = x

for i in range(min(x, y), 0, -1):
    if x % i == 0 and y % i == 0:
        gcd_number = i
        break

for i in range(1, x * y + 1):
    if i % x == 0 and i % y == 0:
        lcm_number = i
        break

print("GCD:", gcd_number)
print("LCM:", lcm_number)
