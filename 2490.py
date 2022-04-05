for i in range(3):
    y = list(map(int, input().split()))
    if(sum(y) == 0):
        print("E")
    elif(sum(y) == 1):
        print("A")
    elif(sum(y) == 2):
        print("B")
    elif(sum(y) == 3):
        print("C")
    elif(sum(y) == 4):
        print("D")
    