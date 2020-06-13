import datetime
N,H,M,T=map(int,input().split())
first_wake=datetime.datetime(year=2020, month=4, day=19, hour=H,minute=M)
d=datetime.timedelta(minutes=T)
now = first_wake + d*(N-1)
print(int(now.strftime("%H")))
print(int(now.strftime("%M")))

