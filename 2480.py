a, b, c = map(int, input().split())

if(a == b == c):
    print(10000+a*1000)
elif(a == b != c or a == c != b):
    print(1000+a*100)
elif(b == c != a):
    print(1000+b*100)
else:
    max = 1
    if(a > max):
        max = a
    if(b > max):
        max = b
    if(c > max):
        max = c
    print(max*100)