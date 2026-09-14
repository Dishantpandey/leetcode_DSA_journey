def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test karke dekhne ke liye:
print(find_gcd(48, 18))  # Output: 6
print(find_gcd(54, 24))  # Output: 6