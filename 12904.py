while(1):
    s = input()
    s = list(s)
    t = input()
    t = list(t)
    if((1 <= len(s) <= 999) and 2 <= len(t) <= 1000 and (len(s) < len(t))):
        break
temp = []
while(1):
    s.append('A')
    if(s == t):
        print(1)
        break
    for i in range(0, len(s)):
        temp.append(s[len(s)-1-i])
    s = temp
    temp = []
    s.append('B')
    if(s == t):
        print(1)
        break    
    if(len(s) > 999 or len(t) > 1000):
        print(0)
        break