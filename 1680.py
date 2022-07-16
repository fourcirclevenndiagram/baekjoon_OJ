t = int(input())

for i in range(t):
    w, n = map(int, input().split())
    drawer = []

    for j in range(n):
        x_i, w_i = map(int, input().split())
        drawer.append([x_i, w_i])

    capacity = 0
    distance = 0
    previous_value = 0
    
    for i in drawer:
        if capacity + i[1] < w:
            distance += i[0] - previous_value
            capacity += i[1]
        elif capacity + i[1] == w:
            distance += (i[0] - previous_value) + i[0] * 2
            capacity = 0
            if drawer.index(i) == n - 1:
                distance -= i[0] * 2
        elif capacity + i[1] > w:
            capacity = i[1]
            distance += (i[0] - previous_value) + i[0] * 2
        previous_value = i[0]
    if drawer.index(i) == (n-1):
        distance += i[0]
    print(distance)