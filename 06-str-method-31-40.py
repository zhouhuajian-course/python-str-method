"""
Python 字符串方法 36-40

@author  : zhouhuajian
@version : v1.0
"""

print("-----------------------")
# 1. 在 sep 最后一次出现的位置拆分字符串，返回一个 3 元组，其中包含分隔符之前的部分、分隔符本身，以及分隔符之后的部分。
print("12:30:15".rpartition(":"))
# 2. 如果分隔符未找到，则返回的 3 元组中包含两个空字符串以及字符串本身。
print("12:30:15".rpartition("-"))
# 3. 注意点：str.partition(sep)，如果分隔符未找到，则返回的 3 元组中包含字符本身以及两个空字符串。
print("12:30:15".partition("-"))
#
#
#
#
#
#
print("-------------------")
# 1. 返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。
print("this.is.a.test.file.py".rsplit("."))
# 2. 如果给出了 maxsplit，则最多进行 maxsplit 次拆分，从 最右边 开始。
print("this.is.a.test.file.py".rsplit(".", maxsplit=2))
# 3. 如果 sep 未指定或为 None，任何空白字符串都会被作为分隔符。
print("this \t\r  is \n  a   test".rsplit())
#
#
#
#
#
#
#
#
#
#
print("---------------------------")
# 1. 返回原字符串的副本，移除其中的末尾字符。 chars 参数为指定要移除字符的字符串。
string = "test*****"
print(string.rstrip("*"))
# 2. 如果省略或为 None，则 chars 参数默认移除空白符。
string = "test \r\t\n   "
print(string.rstrip())
# 3. 实际上 chars 参数并非指定单个后缀；而是会移除参数值的所有组合:
string = "testaabbcc"
print(string.rstrip("abc"))  # {"a", "b", "c"}
#
#
#
#
#
#
#
print("-----------------")
# 1. 返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。
print("this.is.a.test.file.py".split("."))
# 2. 如果给出了 maxsplit，则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）。
print("this.is.a.test.file.py".split(".", maxsplit=2))
# 3. 如果给出了 sep，则连续的分隔符不会被组合在一起而是被视为分隔空字符串 (例如 '1,,2'.split(',') 将返回 ['1', '', '2'])。
print("a..test".split("."))
# 4. sep 参数可能由多个字符组成 (例如 '1<>2<>3'.split('<>') 将返回 ['1', '2', '3'])。 使用指定的分隔符拆分空字符串将返回 ['']。
print("this---is---a---test".split("---"))
# 5. 使用指定的分隔符拆分空字符串将返回 ['']
print('----------')
print("".split("---"))  # 如果有sep，拆分空字符串不是空列表
# 6. 如果 sep 未指定或为 None，则会应用另一种拆分算法：连续的空格会被视为单个分隔符，
print("this \t\r\n is  a  test".split())
# 7. 其结果将不包含开头或末尾的空字符串，如果字符串包含前缀或后缀空格的话。 因此，使用 None 拆分空字符串或仅包含空格的字符串将返回 []。
# print('----------')
print(" \t\r\n this \t\r\n is  a  test  ".split())
# 
# print("".split("<>"))  # 如果有sep，拆分空字符串不是空列表
print("".split())
print("   \t\r\n   ".split())
#
#
#
#
#
#
#
#
#
#
#
#
#
print("-----------------")
# 1. 返回由原字符串中各行组成的列表，在行边界的位置拆分。
print("First Line\nSecond Line\nThird Line\nFourth Line".splitlines())
print("First Line\nSecond Line\nThird Line\nFourth Line".split("\n"))
# 2. 结果列表中不包含行边界，除非给出了 keepends 且为真值。
print("First Line\nSecond Line\nThird Line\nFourth Line".splitlines(keepends=True))
# 3. 此方法会以下列行边界进行拆分。 特别地，行边界是 universal newlines 的一个超集。
print('-------------')
print("First Line\nSecond Line\rThird Line\r\nFourth Line".splitlines())
print("First Line\vSecond Line\fThird Line\x1cFourth Line".splitlines())
# 4. 不同于 split()，当给出了分隔字符串 sep 时，对于空字符串此方法将返回一个空列表，而末尾的换行不会令结果中增加额外的行:
print('-----------------')
print("".splitlines())
print("".split("\n"))
print('-----------------')
print("First Line\nSecond Line\nThird Line\nFourth Line\n".splitlines())
print("First Line\nSecond Line\nThird Line\nFourth Line\n".split("\n"))
# 
