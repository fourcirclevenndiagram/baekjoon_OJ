t = input()
t = int(t)
m = input().split()

ms_flag = 0

for i in range(0, t):
    if(m[i] == 'mumble' or int(m[i]) == i+1):
        ms_flag += 1
if(ms_flag == t):
    print("makes sense")
else:
    print("something is fishy")