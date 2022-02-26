n, k = map(int, input().split())

# old = [0, 1, 0]
# new = []
# for i in range(0, n):
#     new.append(0)
#     for j in range(0, len(old)-1):
#         new.append(old[j] + old[j+1])
#     new.append(0)
#     old = new
#     new = []
#     print(old)
# 
# print(int(old[k+1] % m))

old = [0, 1, 0]
new = []
for i in range(0, n):
    new.append(0)
    for j in range(0, len(old)-1):
        new.append(old[j] + old[j+1])
        if(j == k):
            break
    new.append(0)
    old = new
    new = []
print(int(old[k+1])%1000000007)