a, b = input().split()
a, b = int(a), int(b)
c = input()
c = int(c)
after_cooking = ((a+((b+c)//60))%24, (b+c)%60)
print(after_cooking[0], after_cooking[1])