t = 0
# while(t <= 0):
#     print("t값을 입력해주세요")
#     t = input()
#     t = int(t)
while(1):
    print("t값을 입력해주세요")
    t = input()
    t = int(t)
    if(t >= 0):
        break

for i in range(0, t):
    a, b = 0, 0
    # while(not ((1 <= a and a <= 100) and (1<= b and b <= 1000000))):
    while(1):
        print("a값과 b값을 공백으로 구분하여 입력해주세요")
        a, b = map(int, input().split())
        # a, b = int(a), int(b)
        if((1 <= a and a <= 100) and (1 <= b and b <= 1000000)):
            print((a**b)-((a**b)//10)*10)
            break
