from re import I


a = input()
a = int(a)
while(a != 1):
    i = 2
    while(i <= a):
        if(a % i == 0):
            print(i)
            a /= i
            break
        i += 1