#coding:utf-8
import datetime
N=int(input())
asleep=0
for i in range(N):
    t1_s,t2_s=input().split()
    if int(t1_s.split(":")[0]) > int(t2_s.split(":")[0]): # 日付またぐ
        t1_s="2020-05-21-"+t1_s
        t2_s="2020-05-22-"+t2_s
    else: #日付またがない
        t1_s="2020-05-22-"+t1_s
        t2_s="2020-05-22-"+t2_s
    t1=datetime.datetime.strptime(t1_s, '%Y-%m-%d-%H:%M')
    t2=datetime.datetime.strptime(t2_s, '%Y-%m-%d-%H:%M')
    asleep=asleep + ((t2-t1).seconds//60)
print(asleep)