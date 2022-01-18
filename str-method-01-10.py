"""
Python 字符串方法 01-10

@author  : zhouhuajian
@version : v1.0
"""

print("-" * 10)
print("pytHon sTring meThoD".capitalize())
# python 3.8+与 python 3.7- 的区别
print("ßabc".capitalize())
# python 3.8+ Ss
# python 3.7- SS


print("-" * 10)
print("pytHon sTring meThoD".casefold())
print("ß".casefold())  # 比lower更彻底

print("-" * 10)
print("周华健".center(7))
print("周华健".center(7, "-"))
print("周华健".center(6, "-"))  # 非对齐填充
print("周华健".center(2))

print("-" * 10)
print("today is monday".count("day"))
print("today is monday"[3:])
print("today is monday".count("day", 3))
print("today is monday"[3:5])
print("today is monday".count("day", 3, 5))
print("ababa".count("aba"))  # 非重叠出现

print("-" * 10)
print("汉字".encode(encoding="utf-8"))
# print("汉字".encode(encoding="ascii"))  # 编码错误
print("汉字".encode(encoding="ascii", errors="ignore"))

print("-" * 10)
print("test".endswith("st"))
print("test".endswith("at"))
print("test".endswith(("st", "at")))
# start end 跟 str.count() 用法一样
print("test".endswith("st", 3, 4))

print("-" * 10)
print("Id\tName\tAge\n1\tzhangsan\t18\n2\tlisi\t6".expandtabs(tabsize=10))
print('01\t012\t0123\t01234'.expandtabs())
print('a\tb\tc\td'.expandtabs())
# \n或\r当前列会重设为零
print('01\t012\t0123\t01234\na\tb\tc\td'.expandtabs())
# 每 tabsize 个字符设为一个制表位
# 0123 已经是一个制表位
# 这属于特殊情况
print('01\t012\t0123\t01234'.expandtabs(4))

print("-" * 10)
print("a little girl".find("little"))
# 最小索引 也就是第一个找到的位置
print("a little girl little".find("little"))
print("a little girl".find("kid"))
# start end 跟str.count() str.endswith() 用法一样
print("a little girl little".find("little", 9))

print("-" * 10)
print("The sum of 1 + 2 is {0}".format(1 + 2))
print("他的名字是{0}，今年{1}岁。".format("张三", 18))
print("他的名字是{}，今年{}岁。".format("张三", 18))
print("他的名字是{name}，今年{age}岁。".format(name="张三", age=18))

print("-" * 10)
# 引用的传参方式，字典是可变对象
def format(*args, **kwargs):
    print(hex(id(kwargs)), kwargs)
user_info = dict(name="张三", age=18)
print(hex(id(user_info)), user_info)
format(**user_info)

def format_map(mapping):
    print(hex(id(mapping)), mapping)
user_info = dict(name="张三", age=18)
print(hex(id(user_info)), user_info)
format_map(user_info)

class Default(dict):
    def __missing__(self, key):
        return key
print('{name} was born in {country}'.format_map(Default(name='Zhangsan')))
