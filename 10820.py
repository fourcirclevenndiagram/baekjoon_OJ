import sys
while(1):
    temp = sys.stdin.readline().rstrip('\n')
    sml_l, cap_l, num, spa = 0, 0, 0, 0
    if(len(temp) == 0):
        break
    for i in temp:
        if(i.islower()):
            sml_l += 1
        elif(i.isupper()):
            cap_l += 1
        elif(i.isdigit()):
            num += 1
        elif(i.isspace()):
            spa += 1

    print(sml_l, cap_l, num, spa)
