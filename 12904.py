while(1):
    s = input().strip()
    s = list(s)
    t = input().strip()
    t = list(t)
    if((1 <= len(s) <= 999) and 2 <= len(t) <= 1000 and (len(s) < len(t))):
        break
temp = []
flag = 0
while(1):
    s.append('A')
    print(s)
    if(s == t):
        flag += 1
        break
    for i in range(0, len(s)):
        temp.append(s[len(s)-1-i])
    s = temp
    temp = []
    s.append('B')
    print(s)
    if(s == t):
        flag += 1
        break    
    if(len(s) > 999 or len(t) > 1000):
        break
    print(s)
if(flag):
    print(1)
else:
    print(0)