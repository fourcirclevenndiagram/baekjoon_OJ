t = input()
t = int(t)
for i in range(0, t):
    a, b = input().split()
    a, b = int(a), int(b)
    if(a>b):
        a, b = b, a
    b_copy = b
    while(b % a != 0):
        b += b_copy
    print(b)