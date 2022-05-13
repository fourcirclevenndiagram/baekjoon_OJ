my_name = input()
n = int(input())
drawer = []
max_p = 0
idx = 0
for i in range(n):
    drawer.append(input())
drawer = sorted(drawer)

for i in range(n):
    l = my_name.count("L") + drawer[i].count("L")
    o = my_name.count("O") + drawer[i].count("O")
    v = my_name.count("V") + drawer[i].count("V")
    e = my_name.count("E") + drawer[i].count("E")
    p = ((l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e)) % 100
    if(max_p < p):
        max_p = p
        idx = i
print(drawer[idx])