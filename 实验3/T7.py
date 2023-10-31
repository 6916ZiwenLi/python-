# 用户输入两个点的坐标
point1 = input("请输入第一个点的坐标 (x1, y1)：")
point2 = input("请输入第二个点的坐标 (x2, y2)：")

# 将输入解析为整数坐标
x1, y1 = map(int, point1.split(','))
x2, y2 = map(int, point2.split(','))

# 计算曼哈顿距离
manhattan_distance = abs(x1 - x2) + abs(y1 - y2)

# 输出结果
print("两点之间的曼哈顿距离是:", manhattan_distance)
