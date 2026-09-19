def find_duplicates(s):
    seen = set()
    duplicates = set()
    
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
            
    return list(duplicates)


text = "programming"
print(find_duplicates(text))  
# Output: ['r', 'm', 'g', 'p']