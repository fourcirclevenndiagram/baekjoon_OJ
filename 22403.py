t = input()
t = int(t)
a = []
saigo = ''
henjiMachi = 0
for i in range(0, t):
    kotoba = input()
    if(kotoba == 'A'):
        henjiMachi += 1
    elif(kotoba == 'Un'):
        henjiMachi -= 1
        if(henjiMachi < 0):
            henjiMachi = 0
    saigo = kotoba
if(henjiMachi == 0 and saigo == 'Un'):
    print("YES")
else:
    print("NO")
