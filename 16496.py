n = int(input())
num = list(input().split())

def sol(a):
    for i in range(len(a)-1):
        idx = i
        for j in range(i+1, len(a)):
            if(int(a[j] + a[idx]) > int(a[idx] + a[j])):
                idx = j
        a[i], a[idx] = a[idx], a[i]

sol(num)
ans = ''.join(num)
if num.count('0')==len(num): ans='0'
print(ans)
