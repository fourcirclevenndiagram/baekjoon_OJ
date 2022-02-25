k = int(input())
ans = []
tot = 0
for i in range(k):
    temp = int(input())
    if(temp > 0):
        ans.append(temp)
    elif(temp == 0):
        ans.pop()
for i in range(len(ans)):
    tot += ans[i]
print(tot)