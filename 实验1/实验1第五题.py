
x = input('请输入x的值：')
x = eval(x)
if 0<=x<5:
    print(x)
elif 5<=x<10:
    print(3*x-5)
elif 10<=x<20:
    print(0.5*x-2)
else:
    print(0)
