n = int(input())
the_list = []
for i in range(n):
    the_list.append(input()[0])
the_list = sorted(the_list)
the_set = set(the_list)
drawer = []
for i in the_set:
    if the_list.count(i) >= 5:
        drawer.append(i)
if drawer != []:
    print(''.join(sorted(drawer)))
else:
    print("PREDAJA")

