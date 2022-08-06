n = int(input())

for i in range(1, n+1) :
    tmp = input()
    ans = ''
    for j in range(len(tmp)):
        cod = ord(tmp[j]) + 1
        if cod > 90:
            cod = 65
        ans += chr(cod)
    
    print('String #%d' % i)
    print(ans)