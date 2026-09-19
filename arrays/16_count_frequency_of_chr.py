from collections import Counter

def count_chars_counter(s):
    return dict(Counter(s))


text = "programming"
print(count_chars_counter(text))
# Output: {'p': 2, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}