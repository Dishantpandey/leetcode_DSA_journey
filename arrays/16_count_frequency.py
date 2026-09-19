def find_duplicate_characters(s):
    freq = {}
    

    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    
    duplicates = {char: count for char, count in freq.items() if count > 1}
    
    return duplicates


text = "programming"
print(find_duplicate_characters(text))  
# Output: {'p': 2, 'r': 2, 'g': 2, 'm': 2}
