n = int(input())
cup = [1, 2, 3]
for i in range(n):
    a, b = map(int, input().split())
    aidx, bidx = cup.index(a), cup.index(b)
    cup[aidx], cup[bidx] = cup[bidx], cup[aidx]
    
print(cup[0])