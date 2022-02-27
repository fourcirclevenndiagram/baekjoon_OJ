''' 시간초과로 빠꾸먹은 코드
n = int(input())
deck = []
for i in range(1, n+1):
    deck.append(str(i))
while(len(deck) > 1):
    deck.pop(0)
    if(len(deck) == 1):
        break    
    temp = deck.pop(0)
    deck.append(temp)
deck = ''.join(deck)
print(deck)
'''

''' 테스트코드
def test(n):
    deck = []
    for i in range(1, n+1):
        deck.append(str(i))
    while(len(deck) > 1):
        deck.pop(0)
        if(len(deck) == 1):
            break    
        temp = deck.pop(0)
        deck.append(temp)
    deck = ''.join(deck)
    print(deck)
for i in range(1, 130):
    print("%d, "%i, end='')
    test(i)
'''

n = int(input())
ans = n*2
minus = 1/2
i = 0
while(2**i < n):
    minus *= 2
    i += 1
print(int((n-minus)*2))

    