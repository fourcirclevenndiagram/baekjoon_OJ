n = int(input())
I_wanna_sit = list(map(int, input().split()))
seat = []
get_away = 0
for i in range(n):
    if(not I_wanna_sit[i] in seat):
        seat.append(I_wanna_sit[i])
    else:
        get_away += 1
print(get_away)