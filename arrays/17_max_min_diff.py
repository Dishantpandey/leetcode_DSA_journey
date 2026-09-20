def maxmindiffrence (nums):
    if len(nums) < 2 :
        return []
    max_diff = -1
    min_diff = float("inf")
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            diff = abs(nums[i]-nums[j])
            if diff>max_diff:
                max_diff = diff
            if diff<min_diff:
                min_diff = diff
    return [max_diff,min_diff]



nums = [1,2,3,4,7,5,6]
final_result = maxmindiffrence(nums)
print(final_result)