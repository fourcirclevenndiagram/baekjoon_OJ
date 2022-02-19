import scipy.special
n, k, m = input().split()
n, k, m = int(n), int(k), int(m)
print(int(scipy.special.comb(n, k) % m))