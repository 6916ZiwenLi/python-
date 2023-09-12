# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:11:01 2023

@author: pyf20
"""

n = 1
while 1:
    if n%2==1 and n%3==0 and n%4==1 and n%5==4 and n%6==3 and n%7==0 and n%8==1 and n%9==0:
        print("这里有{}糖果 在盒子里.".format(n))
        break
    else:
        n=n+1
