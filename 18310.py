n = int(input())
idx = int((n-1)/2)
ante = sorted(list(map(int, input().split())))
print(ante[idx])