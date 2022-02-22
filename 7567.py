dish = input()
pre_dish = dish[0]
width = 10
for i in range(1, len(dish)):
    if(pre_dish == dish[i]):
        width += 5
    else:
        width += 10
    pre_dish = dish[i]
print(width)
