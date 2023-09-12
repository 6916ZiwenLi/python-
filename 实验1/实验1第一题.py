# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


year = int(input("输入一个年份: "))
if year%4==0 and year%100!=0 or year %400==0:
    print (year,'是闰年')
else:
    print (year,'不是闰年')
    
    

