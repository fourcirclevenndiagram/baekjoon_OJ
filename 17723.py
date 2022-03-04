import sys
m = int(sys.stdin.readline())
drawer = set()
for i in range(0, m):
    cmd = sys.stdin.readline().split()   
    
    if(len(cmd) == 2):
        cmd[1] = int(cmd[1])
        if(cmd[0] == "add"):
            drawer.add(cmd[1])
        elif(cmd[0] == "remove"):
            drawer.discard(cmd[1])
        elif(cmd[0] == "check"):
            if(cmd[1] in drawer):
                print(1)
            else:
                print(0)
        elif(cmd[0] == "toggle"):
            if(cmd[1] in drawer):
                drawer.discard(cmd[1])
            else:
                drawer.add(cmd[1])
    elif(len(cmd) == 1):        
        if(cmd[0] == "all"):       
            drawer = set([i for i in range(1, 21)])
        elif(cmd[0] == "empty"):
            drawer = set()
