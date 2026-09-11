input_num =int(input("enter a number:"))
if input_num <=1:
    print("not prime")

for i in range(2,input_num):
    if input_num % i == 0:
        print("not prime")
        break
else:
    print("prime")        