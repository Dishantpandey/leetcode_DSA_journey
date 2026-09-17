def combination_sum(candidates, target):
    res = []
    
    def dfs(i, current_comb, current_sum):
        if current_sum == target:
            res.append(list(current_comb))
            return
        
        if current_sum > target or i >= len(candidates):
            return
        
        # Include current element (can reuse, so stay at index `i`)
        current_comb.append(candidates[i])
        dfs(i, current_comb, current_sum + candidates[i])
        current_comb.pop()
        
        # Skip current element and move to next index
        dfs(i + 1, current_comb, current_sum)
        
    dfs(0, [], 0)
    return res

# Test karke dekhne ke liye:
print(combination_sum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
print(combination_sum([2, 3, 5], 8))     # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]