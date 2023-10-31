class Stack:
    def __init__(self, size=10):  # 默认栈大小为10
        self.__content = []  # 使用列表存放元素
        self.__size = size
        self.__current = 0  # 栈中元素个数

    def empty(self):  # 清空栈
        self.__content = []
        self.__current = 0

    def isEmpty(self):  # 判断栈是否为空
        return not self.__content

    def setSize(self, size):  # 调整栈大小
        # 如果调整后大小小于当前已有元素数量
        # 删除多余元素
        if size < self.__current:
            for i in range(size, self.__current)[::-1]:
                del self.__current[i]
        self.__current = size
        self.__size = size

    def isFull(self):  # 判断栈是否满
        return self.__size == self.__current

    def push(self, v):  # 压栈
        if self.__current < self.__size:
            self.__content.append(v)
            self.__current = self.__current + 1
        else:
            print("Steck full!!!")

    def __str__(self):
        return str(self.__current)

    def pop(self):  # 弹栈
        if self.__current:
            self.__current = self.__current - 1
            return self.__content.pop()
        else:
            print("Steck is empty!!!")

    def show(self):
        print(self.__current)

    def showRemainderSpace(self):
        print("Steck can still PUSH", self.__size - self.__current, 'elements')


if __name__ == '__main__':
    sk = Stack(6)
    sk.push(12)
    sk.push(13)
    sk.push(33)
    sk.pop()
    sk.show()
    sk.showRemainderSpace()
