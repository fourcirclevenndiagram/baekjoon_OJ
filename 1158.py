n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
drawer = []
num = k - 1

for i in range(n):
    if len(arr) <= num:
        num = num % len(arr)
        drawer.append(arr.pop(num))
        num = num + k -1
    else:
        drawer.append(arr.pop(num))
        num = num + k - 1

print("<", ', '.join(str(i) for i in drawer), ">", sep = '')