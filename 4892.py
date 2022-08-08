num = 0

while True:
    n = int(input())
    num += 1
    if n == 0:
        break
    if n%2 == 0:
        print(num, ". even ", n//2, sep='')
        print("%d. even %d"%(num, n//2))
    else:
        print(num, ". odd ", n//2, sep='')
        print("%d. odd %d"%(num, n//2))