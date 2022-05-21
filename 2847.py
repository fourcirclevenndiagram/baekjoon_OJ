n = int(input())
ans = 0
scores = []
for i in range(n):
    tmp = int(input())
    scores.append(tmp)
    
for i in range(n-1):
    if(scores[n-i-2] >= scores[n-i-1]):
        ans = ans + scores[n-i-2] - scores[n-i-1] + 1
        scores[n-i-2] = scores[n-i-1] - 1

print(ans)