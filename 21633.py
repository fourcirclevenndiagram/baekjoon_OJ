k = int(input())
ans = round(25 + (k*0.01), 2)

if(ans <= 100):
    print("100.00")
elif(ans >= 2000):
    print("2000.00")
else:
    print(f"{ans:.2f}")