while(1):
    a, b = map(int, input().split())
    if(a != 0 and b == 0):
        print("neither")
        continue
    elif(a == 0 and b == 0):
        break    
    my_c = a % b
    if(my_c == a):
        print("factor")
    elif(my_c == 0):
        print("multiple")
    else:
        print("neither")
