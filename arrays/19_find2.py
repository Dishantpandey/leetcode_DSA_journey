def missingNumber(nums):
    n = len(nums)
    
    # Step 1: 0 se lekar n tak ka total sum nikalne ka formula
    expected_sum = (n * (n + 1)) // 2
    
    # Step 2: Array ke saare numbers ka actual sum nikal lo
    actual_sum = sum(nums)
    
    # Step 3: Dono ka difference hi missing number hai
    return expected_sum - actual_sum

# Test karke dekhte hain:
nums = [3, 0, 1]
print("Missing Number is:", missingNumber(nums))  # Output aayega: 2