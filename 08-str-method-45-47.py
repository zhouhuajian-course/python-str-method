"""
第08课 Python 字符串方法 45-47

@author  : zhouhuajian
@version : v1.0
"""


print("--------------")
# 1. 返回原字符串的副本，其中每个字符按给定的转换表进行映射。 转换表必须是一个使用 __getitem__() 来实现索引操作的对象，通常为 mapping 或 sequence。 当以 Unicode 码位序号（整数）为索引时，转换表对象可以做以下任何一种操作：返回 Unicode 序号或字符串，将字符映射为一个或多个字符；返回 None，将字符从结果字符串中删除；或引发 LookupError 异常，将字符映射为其自身。
string = "abcd".translate({
    "a": "x",
    "b": "y"
})
print(string)
print("--------------")
string = "abcd".translate({
    ord("a"): "x",
    ord("b"): "y"
})
print(string)
print("--------------")
string = "abcd".translate({
    ord("a"): ord("x"),
    ord("b"): "y",
    ord("c"): "也能转成多个字符的字符串",
    ord("d"): None
})
print(string)
# 2. 你可以使用 str.maketrans() 基于不同格式的字符到字符映射来创建一个转换映射表。
# str.maketrans会把字符变成Unicode码位序号
# 推荐str.maketrans()和str.translate()一块使用
print("--------------")
string = "abcd".translate({
    "a": "x",
    "b": "y"
})
print(string)
# #
table = str.maketrans({
    "a": "x",
    "b": "y"
})
print(table)
string = "abcd".translate(table)
print(string)
# print(table)
# 
# 
# 
# 
# 
# 
# 
print("--------------")
# 1. 返回原字符串的副本，其中所有区分大小写的字符 均转换为大写。
print("Washington, Los Angeles, London".upper())
# 2. 请注意如果 s 包含不区分大小写的字符或者如果结果字符的 Unicode 类别不是 "Lu" (Letter, uppercase) 而是 "Lt" (Letter, titlecase) 则 s.upper().isupper() 有可能为 False。
print("Washington, Los Angeles, London".upper().isupper())
print("1234张三李四".upper().isupper())

# 
# 
# 
# 
# 
# 
# 
print("--------------")
# 1. 返回原字符串的副本，在左边填充 ASCII '0' 数码使其长度变为 width。
print("123".zfill(6))
# 2. 正负值前缀 ('+'/'-') 的处理方式是在正负符号 之后 填充而非在之前。
print("+123".zfill(6))
print("-123".zfill(6))
# 3. 如果 width 小于等于 len(s) 则返回原字符串的副本。
print("1234".zfill(3))
# 
# 
