"""
内置函数 dir() 实现了 __dir__() 方法
abc.Mapping
abc.MutableSequence
"""

import keyword
from collections import abc

# NOTE: 缺点是不能处理无效的属性名，如 student = FrozenJSON({'name': 'Jim', 'class': 1}) student.class 会报错
# class FrozenJSON:
#     def __init__(self, mapping) -> None:
#         self.__data = dict(mapping)

#     def __getattr(self, name):
#         try:
#             return getattr(self.__data, name)
#         except AttributeError:
#             return FrozenJSON.build(self.__data[name])

#     def __dir__(self):
#         return self.__data.keys()

#     @classmethod
#     def build(cls, obj):
#         if isinstance(obj, abc.Mapping):
#             return cls(obj)
#         elif isinstance(obj, abc.MutableSequence):
#             return [cls.build(item) for item in obj]
#         else:
#             return obj


# NOTE: 修复无效属性名的问题
class FrozenJSON:
    def __init__(self, mapping) -> None:
        # NOTE: 修复无效属性名的问题
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
                self.__data[key] = value

    def __getattr(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON.build(self.__data[name])

    def __dir__(self):
        return self.__data.keys()

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
