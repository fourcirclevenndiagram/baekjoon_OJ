n = int(input())
candidate = list(map(int, input().split()))
tot_of_decimal = 0
def isThisA(num):
    flag = 0
    if(num == 1):
        flag = 1
    for j in range(2, num//2+1):
        if(num % j == 0):
            flag = 1
            break
    if(flag):
        return 0
    else:
        return 1

for i in candidate:
    tot_of_decimal += isThisA(i)
print(tot_of_decimal)