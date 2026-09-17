def subsets(nums):
    res = []
    
    def dfs(i, current_subset):
        if i == len(nums):
            res.append(list(current_subset))
            return
        
        # Include current element
        current_subset.append(nums[i])
        dfs(i + 1, current_subset)
        current_subset.pop()
        
        # Exclude current element
        dfs(i + 1, current_subset)
        
    dfs(0, [])
    return res

# Test karke dekhne ke liye:
print(subsets([1, 2, 3]))
# Output: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []] (order upar-neeche ho sakta hai)