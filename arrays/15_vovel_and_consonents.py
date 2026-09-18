text = "Hello World"
vowels = "aeiouAEIOU"

v_count = 0
c_count = 0

for char in text:
    if char.isalpha():  # Check karta hai ki ye letter hai ya nahi (space/number ignore karne ke liye)
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")
# Output: Vowels: 3, Consonants: 7