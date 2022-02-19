n = input()
n = int(n)
inp = []
flag = 0
for i in range(0, n):
    sentence = input()
    inp.append(list(sentence))

for i in range(0, n):
    for j in range(0, n):
        if(inp[i][j] != inp[j][i]):
            flag = 1
            break
    if(flag):
        break
if(flag):
    print("NO")
else:
    print("YES")