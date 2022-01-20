"""
第02课 Python 字符串方法 01-10

@author  : zhouhuajian
@version : v1.0
"""

print('----------')
# 1. 首个字符大写，其余为小写
string = "thIS IS a senTENCE."
print(string.capitalize())
# 2. 首个字符大写，不是首个字母大写
string = "1. thIS IS a senTENCE."
print(string.capitalize())
# 3. 如果第一个字符是复合字母类字符，将只有首个字母改为大写，而不再是全部字符大写
# 什么是复合字母类字符？
# ß先转成了ss，再转成大写字母
# python 3.7-，所有字母大写 SS
# python 3.8+，只有首个字母大写 Ss
print("ß".capitalize())
# 查看Unicode 0~9999码位的所有复合字母
for i in range(0, 10000):
    str1 = chr(i)
    str2 = str1.capitalize()
    if len(str2) > 1:
        print(f"{str1}可能是复合字母类字符 {str2}")




print('-------------------')
# 1. 返回原字符串消除大小写的副本
string = "thIS IS a senTENCE."
print(string.casefold())
# 2. 消除大小写类似于转为小写，但是更加彻底一些，因为它会移除字符串中的所有大小写变化形式
print("ß".casefold())
print("ß".lower())



print("-------------------")
# 1. 返回长度为 width 的字符串，原字符串在其正中。 使用指定的 fillchar 填充两边的空位
print("开始".center(8, "="))
# 2. 如果不对称，则剩余的一个字符会添加到左边
print("开始".center(9, "="))
# 3. 默认使用 ASCII 空格符
print("开始".center(8))
# 4. 如果 width 小于等于 len(s) 则返回原字符串的副本
print("开始".center(1, "="))



print('---------------')
# 1. 返回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。 可选参数 start 与 end 会被解读为切片表示法。
string = "number 1, number 2, number 3."
print(string.count("number"))
print(string.count("number", 6))
print(string.count("number", 6, 16))
# string[6:16]
# 2. 非重叠出现
string = "abababab"
print(string.count("aba"))




print('---------------')
# 1. 返回原字符串编码为字节串对象的版本。 默认编码为 'utf-8'。
print("张三".encode())
print("张三".encode(encoding="utf-8"))
# 2. 可以给出 errors 来设置不同的错误处理方案。
# print("张三".encode(encoding="ascii"))  # 报UnicodeEncodeError错误
print("张三".encode(encoding="ascii", errors="ignore"))
print("张三 is a test string".encode(encoding="ascii", errors="ignore"))


print('---------------')
# 1. 如果字符串以指定的 suffix 结束返回 True，否则返回 False。
print("main.py".endswith(".py"))
print("main.py".endswith(".c"))
# 2. suffix 也可以为由多个供查找的后缀构成的元组。
print("main.py".endswith((".py", ".c", ".cpp")))
print("main.py".endswith((".java", ".c", ".cpp")))
# 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较。
print("main.py".endswith(".py", -3))
print("main.py".endswith(".py", 5, 7))









print('---------------')
# 1. 返回字符串的副本，其中所有的制表符会由一个或多个空格替换，具体取决于当前列位置和给定的制表符宽度。
# 每 tabsize 个字符设为一个制表位
string = "Name\tGender\tAge"
# 3个制表位
# 每8个字符设为一个制表位
print(string.expandtabs())
# 3个制表位
# 每10个字符设为一个制表位
print(string.expandtabs(tabsize=10))
# 4个制表位
# 每5个字符设为一个制表位
print(string.expandtabs(tabsize=5))
# 如果字符为换行符 (\n) 或回车符 (\r)，它会被复制并将当前列重设为零。
print('---------')
string = "Name\tGender\tAge\nJack\tmale\t18\nLucy\tfemale\t20"
print(string.expandtabs(tabsize=8))









print('------------')
# 返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引
string = "Friday, Saturday, Sunday"
print(string.find("day"))
print(string.find("day", 8))  # 返回的索引从开头算起，而不是切片的位置
print(string[8:])
print(string.find("day", 8, 16))
print(string[8:16])
#  如果 sub 未被找到则返回 -1
print(string.find("Monday"))






print('----------------------')
# 执行字符串格式化操作。 调用此方法的字符串可以包含字符串字面值或者以花括号 {} 括起来的替换域。 每个替换域可以包含一个位置参数的数字索引，或者一个关键字参数的名称。 返回的字符串副本中每个替换域都会被替换为对应参数的字符串值。
"""
假设有数据
学号 名字  成绩 超过百分之多少的学生
1    Lucy  356  0.8056
要求输出“0001 Lucy 356 80.56%”
"""
# 1. 每个替换域可以包含一个位置参数的数字索引
string = "{0:0>4} {1} {2} {3:.2%}".format(1, "Lucy", 95, 0.8056)
print(string)
# 可以省略位置参数的数字索引，默认从0开始
string = "{:0>4} {} {} {:.2%}".format(1, "Lucy", 95, 0.8056)
print(string)
# 2. 每个替换域可以包含一个位置参数的数字索引，或者一个关键字参数的名称。
string = "{id:0>4} {name} {score} {percentage:.2%}".format(id=1, name="Lucy", score=95, percentage=0.8056)
print(string)
# 可以位置参数的数字索引和关键字参数的名称一块使用
string = "{0:0>4} {1} {score} {percentage:.2%}".format(1, "Lucy", score=95, percentage=0.8056)
print(string)
# 关键字参数可以使用**dict的方式来传递，这是Python的语法糖
student = {
    "id": 1,
    "name": "Lucy",
    "score": 96,
    "percentage": 0.8056
}
string = "{id:0>4} {name} {score} {percentage:.2%}".format(**student)
print(string)


print('--------------------')
# 类似于 str.format(**mapping)，不同之处在于 mapping 会被直接使用而不是复制到一个 dict。
# 1. 类似于 str.format(**mapping)
string = "{id:0>4} {name} {score} {percentage:.2%}".format(**student)
print(string)
string = "{id:0>4} {name} {score} {percentage:.2%}".format_map(student)
print(string)
# 2. 不同之处在于 mapping 会被直接使用而不是复制到一个 dict
# Python中字典是可变变量，传字典给函数或方法，相当于其他语言的传参数引用
print('--------------------')
student = {
    "id": 1,
    "name": "Lucy",
    "score": 96,
    "percentage": 0.8056
}
def format(*args, **kwargs):
    print("接受到数据：")
    print(kwargs)
    kwargs['name'] = 'kathy'
def format_map(mapping):
    print("接受到数据：")
    print(mapping)
    mapping['name'] = 'kathy'
format(**student)
print("学生的数据：")
print(student)
# format_map(student)
# print("学生的数据：")
# print(student)