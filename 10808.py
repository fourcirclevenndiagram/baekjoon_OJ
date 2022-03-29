s = input()
ans = [0] * 26
for i in s:
    tmp = ord(i) - 97
    ans[tmp] += 1
for i in ans:
    print(i, end = ' ')