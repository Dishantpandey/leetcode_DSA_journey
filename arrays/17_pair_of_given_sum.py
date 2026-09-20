def arraysum(nums,target):
    count = 0
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i] + nums[j] == target:
                count +=1
                return[i,j]
    return[]


nums = [1,3,2,2,3,6]
target = 4


result = arraysum(nums,target)
print(result)