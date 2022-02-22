n = int(input())
a = input().split()
tot_score = 0
get_score = 1
for i in range(0, n):
    a[i] = int(a[i])
    flag = 0
    if(a[i] == 1):
        tot_score += get_score
        flag = 1
        get_score += 1
    elif(a[i] == 0):
        flag = 0
        get_score = 1
print(tot_score)
    