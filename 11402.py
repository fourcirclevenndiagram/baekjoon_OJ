n, k, m = input().split()
n, k, m = int(n), int(k), int(m)
# old = [0, 1, 0]
old = [0, 1]
new = []
# for i in range(0, n):
#     new.append(0)
#     for j in range(0, len(old)-1):
#         new.append(old[j] + old[j+1])
#     new.append(0)
#     old = new
#     new = []
for i in range(0, int(n/2)+1):
    if(n % 2 == 1):
        break

print(int(old[k+1] % m))