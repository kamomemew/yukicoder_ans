#!/usr/bin/python3
#coding:utf-8

import re
i=input()
#i="-123++256"
eq=re.match(r"([\+-]*[0-9]*)([\+-]{1})([\+-]*[0-9]*)", i)
x=int(eq.group(1))
op="+" if eq.group(2) == "-" else "-"
y=int(eq.group(3))
print(eval("({x}){op}({y})".format(x=x,op=op,y=y)))