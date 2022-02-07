"""
第05课 Python 字符串方法 31-35

@author  : zhouhuajian
@version : v1.0
"""

print("---------------------")
# 1. 如果字符串以 后缀 字符串结尾，并且 后缀 非空，返回 string[:-len(suffix)] 。
print("a_picture.png".removesuffix(".png"))
# 2. 否则，返回原始字符串的副本：
print("a_picture.png".removesuffix(".jpg"))
# 3. /表示前面的参数只能传位置参数
# print("a_picture.png".removesuffix(suffix=".png"))
#
#
#
#
#
#
#
print("----------------")
# 1. 返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。
string = "Tina has two toys, called Small Tina and Big Tina."
print(string.replace("Tina", "Rachel"))
# 2. 如果给出了可选参数 count，则只替换前 count 次出现。
print(string.replace("Tina", "Rachel", 2))
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
print("----------------------")
# 1. 返回子字符串 sub 在字符串内被找到的最大（最右）索引，这样 sub 将包含在 s[start:end] 当中。 可选参数 start 与 end 会被解读为切片表示法。
string = "twenty one, twenty two, twenty three"
print(string.rfind("twenty"))
# 2. 这样 sub 将包含在 s[start:end] 当中。 可选参数 start 与 end 会被解读为切片表示法。
print(string.rfind("twenty", 12))
print(string.rfind("twenty", 0, 24))
# 3. 如果未找到则返回 -1。
print(string.rfind("thirty"))
#
#
#
#
#
#
#
print("--------------------")
# 类似于 rfind()，但在子字符串 sub 未找到时会引发ValueError。
string = "twenty one, twenty two, twenty three"
print(string.rindex("twenty"))
print(string.rindex("twenty", 12))
print(string.rindex("twenty", 0, 24))
# print(string.rindex("thirty"))
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
print("----------------")
# 1. 返回长度为 width 的字符串，原字符串在其中靠右对齐。 使用指定的 fillchar 填充空位 (默认使用 ASCII 空格符)。
print("test".rjust(10, "*"))
# 2. (默认使用 ASCII 空格符)。
print("test".rjust(10))
# 3. 如果 width 小于等于 len(s) 则返回原字符串的副本。
print("test".rjust(3))
# 
# 
