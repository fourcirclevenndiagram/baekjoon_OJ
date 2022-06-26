yoil = ['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI']
coef = [-1, 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
m, d = map(int, input().split())

d += coef[m]
ans = yoil[d % 7]
print(ans)