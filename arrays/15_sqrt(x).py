def my_sqrt(x):
    if x == 0:
        return 0
        
    left, right = 1, x
    ans = 0
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ans

# Test karke dekhne ke liye:
print(my_sqrt(4))  # Output: 2
print(my_sqrt(8))  # Output: 2 (kyunki 2.828 ka floor 2 hota hai)