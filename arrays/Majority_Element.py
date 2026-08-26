def majorityElement(nums: list[int]) -> int:
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
        
    return candidate


# --- Test Cases ---
def run_tests():
    # Example 1
    assert majorityElement([3, 2, 3]) == 3, "Test 1 Failed"
    
    # Example 2
    assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2, "Test 2 Failed"
    
    # Single element array
    assert majorityElement([1]) == 1, "Test 3 Failed"
    
    # All same elements
    assert majorityElement([5, 5, 5, 5]) == 5, "Test 4 Failed"
    
    # Negative numbers
    assert majorityElement([-1, 1, 1, 1, 2, 1]) == 1, "Test 5 Failed"
    
    print("All test cases passed successfully!")

# Run the tests
if __name__ == "__main__":
    run_tests()