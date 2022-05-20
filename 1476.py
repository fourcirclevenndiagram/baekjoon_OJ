e, s, m = map(int, input().split())
E, S, M = 1, 1, 1
year = 1
while(1):
    if(e == E and s == S and m == M):
        break
    E, S, M = E+1, S+1, M+1
    year += 1
    if(E > 15):
        E -= 15
    if(S > 28):
        S -= 28
    if(M > 19):
        M -= 19

print(year)