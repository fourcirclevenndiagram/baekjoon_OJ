t = int(input())
for i in range(t):
    y, m = map(int, input().split())
    the_y, the_m, the_d = y, m-1, 31
    if(m == 3 and (y%4 != 0 and y < 2100)):
        the_d -= 2
    elif(m == 3 and (y%4 == 0 and y < 2100)):
        the_d -= 3
    elif(m == 5 or m == 7 or m == 10 or m == 12):
        the_d -= 1
    print(the_y, the_m, the_d)