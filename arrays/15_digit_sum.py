number = 12345

# Convert to string, loop through digits, convert back to int, and sum
digit_sum = sum(int(digit) for digit in str(number))

print(digit_sum)  # Output: 15 (1 + 2 + 3 + 4 + 5)