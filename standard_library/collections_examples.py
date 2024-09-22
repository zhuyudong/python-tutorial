from collections import Counter, defaultdict, deque, namedtuple

# NOTE: namedtuple 是一个函数，用来创建一个带字段名的元组
Point1 = namedtuple("Point", "x y")
Point2 = namedtuple("Point", ["x", "y"])

print(Point1(1, 2))  # Point(x=1, y=2)
print(Point2(1, 2))  # Point(x=1, y=2)
print(Point2.x)  # _tuplegetter(0, 'Alias for field number 0')

# NOTE: 双端队列 deque 是一个双向队列，可以从队列的两端添加和删除元素
# 空的双端队列
d1 = deque()
print(d1)  # deque([])
# 从右边添加元素
d1.append(1)
d1.append(2)
# 从左边添加元素
d1.appendleft(3)
d1.appendleft(4)
print(d1)  # deque([4, 3, 1, 2])
# 从右边删除元素
d1.pop()
print(d1)  # deque([4, 3, 1])
# 从左边删除元素
d1.popleft()
print(d1)  # deque([3, 1])
d2 = deque([1, 2, 3])
print(d2)  # deque([1, 2, 3])

# NOTE: Counter是一个计数器，用于统计可迭代对象中元素的数量
c = Counter("hello")
print(c)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
c = Counter(["hello", "world"])
print(c)  # Counter({'hello': 1, 'world': 1})

# NOTE: defaultdict 是一个带有默认值的字典
d = defaultdict(int)
print(d["a"])  # 0
d = defaultdict(lambda: "default")
print(d["a"])  # default

# abc 中实现了若干基类 #
# NOTE: __contains__ 是一个抽象基类，用于判断一个对象是否是容器


class MContainer:
    def __init__(self, data):
        self.data = data

    def __contains__(self, x):
        return x in self.data


c = MContainer([1, 2, 3])
print(1 in c)  # True
print(4 in c)  # False


# NOTE: __iter__ 是一个抽象基类，用于判断一个对象是否是可迭代的
class MIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


c = MIterable([1, 2, 3])
for i in c:
    print(i)  # 1 2 3


# NOTE: __size__ 是一个抽象基类，用于判断一个对象的大小
class MSize:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)


c = MSize([1, 2, 3])
print(len(c))  # 3


# NOTE: __getitem__ 是一个抽象基类，用于判断一个对象是否是映射
class MMapping:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, x):
        return self.data[x]


c = MMapping({"a": 1, "b": 2, "c": 3})
print(c["a"])  # 1
