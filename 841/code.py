#!/usr/bin/python3
#!coding: utf-8
i=input()
sep1st_is_holiday=((i.split()[0]=="Sun")or(i.split()[0]=="Sat"))
sep2nd_is_holiday=((i.split()[1]=="Sun")or(i.split()[1]=="Sat"))
if sep1st_is_holiday and sep2nd_is_holiday:
    print("8/33")
elif sep1st_is_holiday and not sep2nd_is_holiday:
    print("8/32")
else:
    print("8/31")
