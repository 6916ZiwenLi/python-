# 用户输入英文句子
sentence = input("请输入一个英文句子: ")

# 将句子分割成单词
words = sentence.split()
#split() 方法是Python字符串对象的一个内置方法，
# 用于将一个字符串分割成多个子字符串
# 返回一个包含分割结果的列表。
# 通常，split() 方法在提供分隔符的情况下将字符串拆分为多个子字符串。

# 初始化最长单词和其长度
longest_word = ""
max_length = 0

# 遍历单词列表，找到最长的单词
for word in words:
    # 移除标点符号
    word = word.strip('.,?!')
    #strip() 方法是Python字符串对象的内置方法，#
    # 用于去除字符串的前导（开头）和尾随（结尾）空白字符（包括空格、制表符、换行符等）。
    # 这个方法返回一个新的字符串，其中去除了指定的空白字符。
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

# 输出最长的单词和其长度
print("最长的单词是:", longest_word)
print("长度为:", max_length)
