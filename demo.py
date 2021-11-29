class MyClass:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    def __add__(self, others):
        return MyClass(self.height + others.height, self.weight + others.weight)
    def __sub__(self, others):
        return MyClass(self.height - others.height, self.weight - others.weight)
    def intro(self):
        print("高为", self.height, "重为", self.weight)

def main():
    a = MyClass(10, 5)
    a.intro()

    b = MyClass(20, 10)
    b.intro()

    c = b - a
    c.intro()

    d = a + b + c
    d.intro()

if __name__ == '__main__':
    main()
