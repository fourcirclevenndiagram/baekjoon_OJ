temp = 'oh, yes, yes'
while(temp != '0'):
    temp = input()
    length = len(temp)
    flag = 0
    for i in range(length//2):
        if(temp[i] != temp[length-i-1]):
            flag = 1
            break
    if(flag):
        print('no')
    else:
        print('yes')