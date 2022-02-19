######## 테스트를 위한 코드 ########
import random
a = 5
drawer = []
mixed_drawer = []
for i in range(0, a):
    drawer.append(i+1)
for i in range(0, a):
    temp = drawer.pop(random.randint(0, len(drawer)-1))
    mixed_drawer.append(temp)
for i in range(0, a-1):
    temp = mixed_drawer[i] + mixed_drawer[i+1]
    drawer.append(temp)

######## 테스트를 위한 코드 끝 ########