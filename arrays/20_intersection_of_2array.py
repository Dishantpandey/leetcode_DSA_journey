def findIntersection(arr1, arr2):
    ans = []
    
    # Pehle array ke har ek number par loop chalayenge
    for num in arr1:
        # 2 conditions check karenge:
        # 1. Kya wo number arr2 ke andar bhi maujood hai? (num in arr2)
        # 2. Kya wo hamari ans list mein pehle se nahi hai? (num not in ans - duplicates se bachne ke liye)
        if num in arr2 and num not in ans:
            ans.append(num)
            
    return ans

# Test karke dekhte hain:
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print("Intersection:", findIntersection(arr1, arr2))  # Output aayega: [2]