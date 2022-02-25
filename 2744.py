n = input()
n = list(n)
for i in range(len(n)):
    if(65 <= ord(n[i]) and ord(n[i]) <= 90):
        n[i] = chr(ord(n[i])+32)
    elif(97 <= ord(n[i]) and ord(n[i]) <= 122):
        n[i] = chr(ord(n[i])-32)
    
n = ''.join(n)
print(n)