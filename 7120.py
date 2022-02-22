n = input()
ans = []
ans.append(n[0])
for i in range(1, len(n)):
    if(n[i] != n[i-1]):
        ans.append(n[i])
ans = ''.join(ans)
print(ans)