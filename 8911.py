t = int(input())

for i in range(t):
    pos = [0, 0]
    direction = 'North'
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    my_order = list(input())
    for j in my_order:
        if(direction == 'North'):
            if(j == 'F'):
                pos[1] += 1
            elif(j == 'B'):
                pos[1] -= 1
            elif(j == 'L'):
                direction = 'West'
            elif(j == 'R'):
                direction = 'East'
        elif(direction == 'South'):
            if(j == 'F'):
                pos[1] -= 1
            elif(j == 'B'):
                pos[1] += 1
            elif(j == 'L'):
                direction = 'East'
            elif(j == 'R'):
                direction = 'West'
        elif(direction == 'East'):
            if(j == 'F'):
                pos[0] += 1
            elif(j == 'B'):
                pos[0] -= 1
            elif(j == 'L'):
                direction = 'North'
            elif(j == 'R'):
                direction = 'South'
        elif(direction == 'West'):
            if(j == 'F'):
                pos[0] -= 1
            elif(j == 'B'):
                pos[0] += 1
            elif(j == 'L'):
                direction = 'South'
            elif(j == 'R'):
                direction = 'North'
        max_x = max(max_x, pos[0])
        max_y = max(max_y, pos[1])
        min_x = min(min_x, pos[0])
        min_x = min(min_x, pos[1])
        print(pos, direction)
    range_x = max_x - min_x
    range_y = max_y - min_y
    
    print(range_x * range_y)