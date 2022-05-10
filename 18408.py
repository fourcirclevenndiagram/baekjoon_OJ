drawer = map(int, input().split())
c1 = drawer.count(1)
c2 = drawer.count(2)
if(c1 > c2):
    print(1)
elif(c1 < c2):
    print(2)