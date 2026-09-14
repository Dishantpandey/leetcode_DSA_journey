def check_perfect_number(num):
    if num <= 1:
        return False
        
    total_sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            total_sum += i
            if i * i != num:
                total_sum += num // i
        i += 1
        
    return total_sum == num

# Test karke dekhne ke liye:
print(check_perfect_number(28))  # Output: True (28 ke proper divisors 1, 2, 4, 7, 14 hain, aur sabka sum 28 hai)
print(check_perfect_number(6))   # Output: True
print(check_perfect_number(12))  # Output: False