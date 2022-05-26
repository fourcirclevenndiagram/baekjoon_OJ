import datetime
t1, t2, t3 = map(int, input().split())
d1, d2, d3 = map(int, input().split())

raw_data = list(str(datetime.date(d1,d2,d3)-datetime.date(t1,t2,t3)).split())
d_day = int(raw_data[0])
days = 0 
for i in range(0,1000):
    if(i%400==0):
        days +=366
    elif(i%100==0):
        days += 365
    elif(i%4==0):
        days += 366
    else:
        days += 365
if(d_day >= days):
    print("gg")
else :
    print("D-%d"%d_day)