def unionarray (arr1 , arr2):
    ans3 =[]
    for i in range (len(arr1)):
        if arr1[i] not in ans3:
            ans3.append(arr1[i])
    for i in range (len(arr2)):
        if arr2[i] not in ans3:
            ans3.append(arr2[i])
    return ans3
arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]
result = unionarray(arr1,arr2)
print(result)
