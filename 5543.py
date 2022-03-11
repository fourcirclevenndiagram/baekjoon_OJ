a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
burger_min = a
drink_min = x
if(b < burger_min):
    burger_min = b
if(c < burger_min):
    burger_min = c
if(y < drink_min):
    drink_min = y
print(burger_min+drink_min-50)
