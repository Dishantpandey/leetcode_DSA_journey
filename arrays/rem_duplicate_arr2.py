def remove_dupli2(nums):
    # Agar array ki length 2 ya usse kam hai toh wahi length return kar do
    if len(nums) <= 2:
        return len(nums)
        
    k = 2
    
    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
            
    return k