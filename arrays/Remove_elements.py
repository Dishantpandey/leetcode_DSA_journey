"""def Removeelements (num,val):
    k=0
    for i in range (len(num)):
        if num[i]!=val:
            num[k]=num[i]
            k+=1 
    return k        




num=[3,2,2,3,5,6,6,6,6,54,4,5,6,4,3]
val=3       
print(Removeelements(num,val))
print("Modified list:", num)"""


def removeduplicate(num):
    k=0
    for i in range(len(num)):
        if num[i] != num[k]:
            k += 1
            num[k] = num[i]
    return k + 1


num = [1, 1, 2, 2, 3, 4, 4, 5]
print(removeduplicate(num))
print("Modified list:", num)
