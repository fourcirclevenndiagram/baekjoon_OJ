a, b = input().split()
a, b = list(a), list(b)
for i in range(0, int(len(a)/2)):
    a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]
for i in range(0, int(len(b)/2)):
    b[i], b[len(b)-i-1] = b[len(b)-i-1], b[i]
a = ''.join(a)
b = ''.join(b)
a, b = int(a), int(b)
if(a < b):
    print(b)
elif(b > a):
    print(a)
print(a, b, a<b, a>b)