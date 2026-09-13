def is_armstrong(n):
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n