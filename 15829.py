l = int(input())
key_word = input()
ans = 0
for i in range(0, l):
    ans += (ord(key_word[i])-96)*(31**i)
print(ans%1234567891)