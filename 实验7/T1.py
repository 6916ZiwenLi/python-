class Cylinder:
    num = 3.14

    def __init__(self, a, b):
        self.r = a
        self.h = b

    def volume(self):
        r = float(self.r)
        h = float(self.h)
        self.v = r * r * h * Cylinder.num

    def print(self):
        print(self.v)


if __name__ == "__main__":
    a = input("请输入圆柱体半径:")
    b = input("请输入圆柱体的高:")
    c1 = Cylinder(a, b)
    c1.volume()
    print("圆柱体的体积为:", end='')
    c1.print()
