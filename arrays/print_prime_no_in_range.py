n = int(input("Enter a number: "))
prime_list = []

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(num)

print("Prime numbers list:", prime_list)