"""
Python 字符串方法 11-20

@author  : zhouhuajian
@version : v1.0
"""

print("-" * 10)
print("张三是个小孩，张三今年8岁。".index("张三"))
print("张三是个小孩，张三今年8岁。".index("张三", 7, 14))
# 找不到不报错，find找不到返回-1
# print("张三是个小孩，张三今年8岁。".index("张三", 9))
print("张三是个小孩，张三今年8岁。".find("张三", 9))

print("-" * 10)
print("abcd1234".isalnum())
print("abcd".isalnum())
print("1234".isalnum())
print("".isalnum())
print("abcd1234!@#".isalnum())

print("-" * 10)
print("abcd".isalpha())
print("abcd1234".isalpha())
print("".isalpha())

print("-" * 10)
print("abcd123!@# ".isascii())
print("".isascii())
print("abcd123!@# 汉字".isascii())

print("-" * 10)
print("1234".isdecimal())  # 普通数字
print("１２３４".isdecimal())  # 全角数字
print("①②③④".isdecimal())  # 圆圈数字
print("一二三四".isdecimal())  # 汉字数字

print("ⅠⅡⅢⅣ".isdecimal())  # 罗马数字
print("1234abcd".isdecimal())
print("".isdecimal())

print("-" * 10)
print("1234".isdigit())  # 普通数字
print("１２３４".isdigit())  # 全角数字
print("①②③④".isdigit())  # 圆圈数字
print("一二三四".isdigit())  # 汉字数字
print("ⅠⅡⅢⅣ".isdigit())  # 罗马数字
print("1234abcd".isdigit())
print("".isdecimal())

print('-' * 10)
print("var_01".isidentifier())
print("_test".isidentifier())
print("0123_test".isidentifier())

print('-' * 10)
print("abcd".islower())
# 可以加其他字符，只要所有字母是小写
print("abcd1234".islower())
print("abcd汉字".islower())
print("abcdABCD".islower())
print("1234汉字".islower())

print("-" * 10)
print("1234".isnumeric())  # 普通数字
print("１２３４".isnumeric())  # 全角数字
print("①②③④".isnumeric())  # 圆圈数字
print("一二三四".isnumeric())  # 汉字数字
print("ⅠⅡⅢⅣ".isnumeric())  # 罗马数字
print("1234abcd".isnumeric())
print("".isnumeric())

print("-" * 10)
print("1234abcd汉字".isprintable())
# ASCII码中第0～31号及第127号(共33个)是控制字符
# 控制字符一般不可打印
# 不可打印，可简单理解为打印机打印不出这个字符
print("\t".isprintable())
print("\n".isprintable())
print("\r".isprintable())
print("\b".isprintable())
# 例外情况是 ASCII 空格字符 (0x20) 被视作可打印字符
print("1234 abcd 汉字".isprintable())

