n = int(input())
m = int(input())
ioi = input()
p = "IO"*n + "I"
ans = 0

for i in range(m - len(p)):
    if(ioi[i] == 'I'):
        if(ioi[i:i+len(p)] == p):
            ans += 1
print(ans)