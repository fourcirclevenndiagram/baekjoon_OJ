import statistics
from collections import Counter

n = int(input())
tot = 0
drawer = []
most_frequent = 0
for i in range(0, n):
    drawer.append(int(input()))
    tot += drawer[i]
drawer.sort()
wanted_data = Counter(drawer).most_common()
if((len(wanted_data) == 1)):
    most_frequent = wanted_data[0][0]
elif((len(wanted_data) > 1)):
    if(wanted_data[0][1] == wanted_data[1][1]):
        most_frequent = wanted_data[1][0]
    else:
        most_frequent = wanted_data[0][0]

print(round(tot/n))
print(statistics.median(drawer))
print(most_frequent)
print(drawer[n-1]-drawer[0])