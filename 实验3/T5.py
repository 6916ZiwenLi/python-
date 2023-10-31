# 用户输入列表
user_input = input("请输入一个列表，元素之间用逗号分隔： ")
input_list = [int(x) for x in user_input.split(',')]

# 用户输入两个整数下标
start_index = int(input("请输入开始下标： "))
end_index = int(input("请输入结束下标： "))

# 使用切片获取子列表
if 0 <= start_index < len(input_list) and 0 <= end_index < len(input_list):
    sub_list = input_list[start_index:end_index + 1]
    print("子列表：", sub_list)
else:
    print("下标越界，请输入有效的下标。")
