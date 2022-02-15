"""
第07课 Python 字符串方法 41-44

@author  : zhouhuajian
@version : v1.0
"""

print("--------------")
# 1. 如果字符串以指定的 prefix 开始则返回 True，否则返回 False。
string = "abctest"
print(string.startswith("abc"))
print(string.startswith("123"))
# 2. prefix 也可以为由多个供查找的前缀构成的元组。
print(string.startswith(("abc", "123", "456")))
# 3. 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较
print(string.startswith("bc", 1))
print(string.startswith("bc", 1, 5))





print("--------------")
# 1. 返回原字符串的副本，移除其中的前导和末尾字符。 chars 参数为指定要移除字符的字符串。
print("****test****".strip("*"))
# 2. 如果省略或为 None，则 chars 参数默认移除空白符。
print(" \t\r\n test \t\r\n ".strip())
# 3. 实际上 chars 参数并非指定单个前缀或后缀；而是会移除参数值的所有组合:
# 最外侧的前导和末尾 *chars* 参数值将从字符串中移除。 开头端的字符的移除将在遇到一个未包含于 *chars* 所指定字符集的字符时停止。 类似的操作也将在结尾端发生。 例如:
print("ccaabbtestccaabb".strip("abc"))  # {"a", "b", "c"}







print("--------------")
# 1. 返回原字符串的副本，其中大写字符转换为小写，反之亦然。
print("abcdEFGH".swapcase())
# 2. 请注意 s.swapcase().swapcase() == s 并不一定为真值。
print('-------------')
for i in range(0, 10000):
    single_char_string = chr(i)
    if single_char_string.swapcase().swapcase() != single_char_string:
        print(single_char_string, end=" ")
print()
print('-------------')
print("ß".swapcase())  # ß ss 两个大写的SS
print("ß".swapcase().swapcase())  # 两个小写的ss
print("ß".swapcase().swapcase() == "ß")
# 3. 这里的大小写字符转换不不只是A-Z和a-z的转换，是全球各个国家大小写字符的转换






print("--------------")
# 1. 返回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写。
print("Can Adam win the world champion?".title())
print("Can Adam WIN the wORld chAMpIOn?".title())
# 2. 该算法使用一种简单的与语言无关的定义，将连续的字母组合视为单词。 该定义在多数情况下都很有效，但它也意味着代表缩写形式与所有格的撇号也会成为单词边界，这可能导致不希望的结果:
print("they're bill's friends from the UK".title())

