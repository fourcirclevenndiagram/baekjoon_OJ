n = int(input())
m = int(input())
broken_button = map(int, input().split())

cur_channel = 100
push_button = 0
button_stack = []
def push_plus():
    global cur_channel
    cur_channel += 1
def push_minus():
    global cur_channel
    cur_channel -= 1
def push_num(num):
    global cur_channel
    button_stack.append(str(num))
    
while(cur_channel != n):
    if(n > cur_channel):
        push_plus()
        push_button += 1
    elif(n < cur_channel):
        push_minus()
        push_button += 1

print(push_button)