n = input()
length = len(n)
flag = 0
for i in range(1, length):
    if(flag == 1):
        break
    a, b = n[:i], n[i:]
    ans_a, ans_b = 1, 1
    for j in range(len(a)):
        ans_a *= int(a[j])
    for j in range(len(b)):
        ans_b *= int(b[j])
    if(ans_a == ans_b):
        flag = 1
if(flag):
    print("YES")
else:
    print("NO")