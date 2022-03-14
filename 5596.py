a, b, c, d = map(int,input().split())
e, f, g, h = map(int,input().split())
alex = a+b+c+d
betty = e+f+g+h

if(alex > betty):
    print(alex)
elif(alex < betty):
    print(betty)
