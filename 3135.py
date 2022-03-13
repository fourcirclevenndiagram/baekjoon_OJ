a, b = map(int, input().split())
n = int(input())
channel = []
ans = 1000000000
for i in range(n):    
    channel.append(int(input()))


for i in range(n):
    if(abs(channel[i] - b) < abs(ans - b)):
        ans = channel[i]

turn_chn = 1
if(ans > b):
    turn_chn += ans - b
else:
    turn_chn -= ans - b

if(abs(a - b) < turn_chn):
    print(abs(a - b))
else:
    print(turn_chn)