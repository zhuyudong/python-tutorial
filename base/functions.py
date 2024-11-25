"""
一等对象：
    1. 在运行时创建
    2. 能赋值给变量或数据结构中的元素
    3. 能作为参数传给函数
    4. 能作为函数的返回结果

9 种可调用对象：
    1. 用户定义的函数：使用 def 或 lambda 创建的函数
    2. 内置函数：使用 C 语言（CPython）实现的函数，如 len 或 time.strftime
    3. 内置方法：使用 C 语言实现的方法，如 dict.get
    4. 方法：在类的定义体中定义的函数
    5. 类：调用类时运行类的 __new__ 方法创建一个实例，然后运行 __init__ 方法，初始化实例，最后把实例返回给调用方
    6. 类的实例：如果类定义了 __call__ 方法，那么它的实例可以作为函数调用
    7. 生成器函数：使用 yield 关键字的函数或方法。调用生成器函数返回的是生成器对象
    8. 原生协程函数：使用 async def 定义的函数，调用返回一个协程对象
    9. 异步生成器函数：使用 async def 和 yield 的函数，调用返回一个异步生成器，供 async for 语句使用
生成器、原生协程和异步生成器函数的返回值不是应用程序数据，需要进一步处理的对象
原生协程和异步生成器函数只能由异步编程框架（如 asyncio）使用
"""

import operator
import random
import unicodedata
from collections import namedtuple
from functools import partial, reduce
from operator import add, attrgetter, itemgetter, methodcaller, mul


# NOTE: 7.2 把函数视为对象 #
def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))  # 1405006117752879898543142606244511569936384000000000
# NOTE: 函数对象有 __doc__ 属性，返回函数定义体
print(factorial.__doc__)  # return n!

fact = factorial
print(fact)  # <function factorial at 0x7f8b3b3b7d30>
print(fact(5))  # 120
print(map(factorial, range(11)))  # <map object at 0x7f8b3b3b7d90>
print(
    list(map(fact, range(11)))
)  # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# NOTE: 7.3 高阶函数 #
fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
print(
    sorted(fruits, key=len)
)  # ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']


def reverse(word):
    return word[::-1]


print(reverse("testing"))  # gnitset
print(
    sorted(fruits, key=reverse)
)  # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

print(reduce(add, range(100)))  # 4950
print(sum(range(100)))  # 4950

# NOTE: all 有一个为 False 结果就返回 False， any 有一个为 True 结果就返回 True
print(all([]))  # True
print(any([]))  # False

# NOTE: 7.4 匿名函数 #
fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
# NOTE: word[::-1] 反转字符串排序
print(
    sorted(fruits, key=lambda word: word[::-1])
)  # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

# NOTE: 7.5 9种可调用对象 #


# NOTE: 7.6 用户定义的可调用类型 #
class BingoCage:
    # 接受任何可迭代对象
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())  # 1
print(bingo())  # 0
print(callable(bingo))  # True


# NOTE: 从位置参数到仅限关键字参数 #
# content 标签子元素 class_ 仅限关键字参数
def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs["class"] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)
    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>" for c in content)
        return "\n".join(elements)
    else:
        return f"<{name}{attr_str} />"


print(tag("br"))  # <br />
print(tag("p", "hello"))  # <p>hello</p>
print(tag("p", "hello", "world"))
# <p>hello</p>
# <p>world</p>
print(tag("p", "hello", id=33))  # <p id="33">hello</p>
print(tag("p", "hello", "world", class_="sidebar"))
# <p class="sidebar">hello</p>
# <p class="sidebar">world</p>
print(tag(content="testing", name="img"))


# -------------------------------------------------------------------------------------------------------- #
# NOTE: 支持函数式编程的包 #
def factorial1(n: int):
    return reduce(lambda a, b: a * b, range(1, n + 1))


# NOTE: 使用 operator.mul 替代 lambda a, b: a * b
def factorial2(n: int):
    return reduce(mul, range(1, n + 1))


metro_data = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),  # <1>
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

# NOTE: 使用 itemgetter 对元祖排序
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
# ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833))
# ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
# ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
# ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))

LatLon = namedtuple("LatLon", "lat lon")
Metropolis = namedtuple("Metropolis", "name cc pop coord")
metro_areas = [
    Metropolis(name, cc, pop, LatLon(lat, lon))
    for name, cc, pop, (lat, lon) in metro_data
]
print(
    metro_areas[0]
)  # Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLon(lat=35.689722, lon=139.691667))
print(metro_areas[0].coord.lat)  # 35.689722
name_lat = attrgetter("name", "coord.lat")
for city in sorted(metro_areas, key=attrgetter("coord.lat")):
    print(name_lat(city))
# ('São Paulo', -23.547778)
# ('Mexico City', 19.433333)
# ('Delhi NCR', 28.613889)
# ('Tokyo', 35.689722)
# ('New York-Newark', 40.808611)

# NOTE: operator 中包含的函数列表
operator_funcs = [name for name in dir(operator) if not name.startswith("_")]
print(operator_funcs)
# ['abs', 'add', 'and_', 'attrgetter', 'call', 'concat', 'contains', 'countOf', 'delitem', 'eq', 'floordiv',
# 'ge', 'getitem', 'gt', 'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul',
# 'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 'is_not', 'isub', 'itemgetter',
# 'itruediv', 'ixor', 'le', 'length_hint', 'lshift', 'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne',
# 'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']

# NOTE: 使用 operator.methodcaller 绑定函数
s = "This time has come"
upcase = methodcaller("upper")
print(upcase(s))  # THIS TIME HAS COME

hyphenate = methodcaller("replace", " ", "-")
print(hyphenate(s))  # This-time-has-come

print(str.upper(s))  # THIS TIME HAS COME

# NOTE: 使用 partial 冻结参数
triple = partial(mul, 3)
print(triple(7))  # 21
# 3*1,3*2,3*4,...
print(list(map(triple, range(1, 10))))  # [3, 6, 9, 12, 15, 18, 21, 24, 27]

# NOTE: 规范化函数
nfc = partial(unicodedata.normalize, "NFC")
s1 = "café"
s2 = "cafe\u0301"
print(s1 == s2)  # False
print(nfc(s1) == nfc(s2))  # True
