#!/usr/bin/python3

def regress(list_of_int):
    if len(list_of_int)==1:
        if list_of_int[0]%9==0:
            if not list_of_int[0]==0:
                return 9
            else:
                return 0
        else:
            return list_of_int[0]%9
    new_list=[]
    for i in range(len(list_of_int)-1):
        new_list.append(list_of_int[i]+list_of_int[i+1])
    return regress(new_list)


N=int(input())


for _i in range(N):
    in_num_list=[int(n) for n in input()]
    print(regress(in_num_list))
