lst = [0,0,0,0,0,0,0,0,0,0]
for x in range(10):
    lst[x] = int(input(f"enter {x} no item : "))
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
