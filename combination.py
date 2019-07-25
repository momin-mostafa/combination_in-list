lst = [0,0,0,0,0,0,0,0,0,0]
lst[0] = int(input("1st item of list : "))
lst[1] = int(input("2nd item of list : "))
lst[2] = int(input("3rd item of list : "))
lst[3] = int(input("4rt item of list : "))
lst[4] = int(input("5th item of list : "))
lst[5] = int(input("6th item of list : "))
lst[6] = int(input("7th item of list : "))
lst[7] = int(input("8th item of list : "))
lst[8] = int(input("9th item of list : "))
lst[9] = int(input("10th item of list : "))
print(lst)
print('\n')
sum = int(input("input the sum :"))
print('\n')
for num in lst:
    a = num
    b = sum - a
    if b in lst:
        c = a+b
        print(c,'=',a,'+',b)
    else:
        print(f"combination did not match to {sum}")
