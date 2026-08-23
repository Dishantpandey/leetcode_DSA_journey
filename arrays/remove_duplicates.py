def removeduplicate(num):
    k=0
    for i in range(len(num)):
        if num[i] != num[k]:
            k += 1
            num[k] = num[i]
    return k+1


num = [1, 1, 2, 2, 3, 3]
print(removeduplicate(num))
print("Modified list:", num)