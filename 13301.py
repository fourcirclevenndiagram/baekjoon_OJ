n = int(input())
drawer = [0] * 80
drawer[0], drawer[1] = 1, 1

for i in range(2,n):
    drawer[i] = drawer[i-1]+drawer[i-2]
r = drawer[n-1] + drawer[n-1] + drawer[n-2]

print(r*2)