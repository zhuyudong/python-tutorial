class A:
    def ping(self):
        print("ping:", self)


class B:
    def ping(self):
        print("ping", self)


class MyClass(A, B):
    x = 42

    def x2(self):
        return self.x * 2


# NOTE: 使用 type 动态创建类
MyClass2 = type("MyClass", (A, B), {"x": 42, "x2": lambda self: self.x * 2})

print(MyClass.__name__ == MyClass2.__name__)  # True
print(type(7))  # <class 'int'>
print(type(int))  # <class 'type'>
print(OSError)  # <class 'OSError'>


class Whatever:
    pass


print(type(Whatever))  # <class 'type'>
