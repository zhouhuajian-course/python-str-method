"""
Python 字符串方法 41-47

@author  : zhouhuajian
@version : v1.0
"""
# 
# print("--------------")
# 1. 如果字符串以指定的 prefix 开始则返回 True，否则返回 False。
# string = "Big Event: The Olympic Games will begin next week!"
# print(string.startswith("Big Event"))
# 2. prefix 也可以为由多个供查找的前缀构成的元组。
# print(string.startswith(("Big Event", "Big News", "Breaking News")))
# print(string.startswith(("Big News", "Breaking News")))
# 3. 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较
# print(string.startswith("Big Event", 4))
# print(string.startswith("Big Event", 4, 9))
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
# print("--------------")
# 1. 返回原字符串的副本，移除其中的前导和末尾字符。 chars 参数为指定要移除字符的字符串。
# print("****test****".strip("*"))
# 2. 如果省略或为 None，则 chars 参数默认移除空白符。
# print(" \t\r\n test \t\r\n ".strip())
# 3. 实际上 chars 参数并非指定单个前缀或后缀；而是会移除参数值的所有组合:
# 最外侧的前导和末尾 *chars* 参数值将从字符串中移除。 开头端的字符的移除将在遇到一个未包含于 *chars* 所指定字符集的字符时停止。 类似的操作也将在结尾端发生。 例如:
# print("ccaabbtestccaabb".strip("abc"))
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
# print("--------------")
# 1. 返回原字符串的副本，其中大写字符转换为小写，反之亦然。
# print("abcdEFGH".swapcase())
# 2. 请注意 s.swapcase().swapcase() == s 并不一定为真值。
# print('-------------')
# for i in range(0, 10000):
#     single_char_string = chr(i)
#     if single_char_string.swapcase().swapcase() != single_char_string:
#         print(single_char_string, end=" ")
# print()
# print('-------------')
# print("ß".swapcase())  # 两个大写的SS
# print("ß".swapcase().swapcase())  # 两个小写的ss
# print("ß".swapcase().swapcase() == "ß")
# 3. 这里的大小写字符转换不不只是A-Z和a-z的转换，是全球各个构架大小写字符的转换
# 
# 
# 
# 
# 
# 
# 
# print("--------------")
# 1. 返回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写。
# print("Can Adam win the world champion?".title())
# print("Can Adam WIN the wORld chAMpIOn?".title())
# 2. 该算法使用一种简单的与语言无关的定义，将连续的字母组合视为单词。 该定义在多数情况下都很有效，但它也意味着代表缩写形式与所有格的撇号也会成为单词边界，这可能导致不希望的结果:
# print("they're bill's friends from the UK".title())
# 
# 
# 
# 
# 
# 
# 
# 
# print("--------------")
# 1. 返回原字符串的副本，其中每个字符按给定的转换表进行映射。 转换表必须是一个使用 __getitem__() 来实现索引操作的对象，通常为 mapping 或 sequence。 当以 Unicode 码位序号（整数）为索引时，转换表对象可以做以下任何一种操作：返回 Unicode 序号或字符串，将字符映射为一个或多个字符；返回 None，将字符从结果字符串中删除；或引发 LookupError 异常，将字符映射为其自身。
# # "张三，李四，王五" -> "zhang3李4王五"
# translation_table = {
#     0x5f20: "zhang",  # 张->zhang
#     0x4e09: 0x33,  # 三->3
#     0xff0c: None,  # ，->
#     0x56db: "4"  # 四->4
# }
# print("张三，李四，王五".translate(translation_table))
# 2. 如果键是字符，没有转换效果
# translation_table = {
#     "张": "zhang",  # 张->zhang
#     "三": 0x33,  # 三->3
#     0xff0c: None,  # ，->
#     0x56db: "4"  # 四->4
# }
# print("张三，李四，王五".translate(translation_table))
# 2. 你可以使用 str.maketrans() 基于不同格式的字符到字符映射来创建一个转换映射表。
# str.maketrans会把字符变成Unicode码位序号
# 推荐str.maketrans()和str.translate()一块使用
# print("--------------")
# translation_table = str.maketrans({
#     "张": "zhang",  # 张->zhang
#     "三": 0x33,  # 三->3
#     0xff0c: None,  # ，->
#     0x56db: "4"  # 四->4
# })
# print(translation_table)
# print("张三，李四，王五".translate(translation_table))
# 
# 
# 
# 
# 
# 
# 
# print("--------------")
# 1. 返回原字符串的副本，其中所有区分大小写的字符 均转换为大写。
# print("Washington, Los Angeles, London".upper())
# 2. 请注意如果 s 包含不区分大小写的字符或者如果结果字符的 Unicode 类别不是 "Lu" (Letter, uppercase) 而是 "Lt" (Letter, titlecase) 则 s.upper().isupper() 有可能为 False。
# print("Washington, Los Angeles, London".upper().isupper())
# print("1234张三李四".upper().isupper())
# 
# 
# 
# 
# 
# 
# 
# print("--------------")
# 1. 返回原字符串的副本，在左边填充 ASCII '0' 数码使其长度变为 width。
# print("123".zfill(6))
# 2. 正负值前缀 ('+'/'-') 的处理方式是在正负符号 之后 填充而非在之前。
# print("+123".zfill(6))
# print("-123".zfill(6))
# 3. 如果 width 小于等于 len(s) 则返回原字符串的副本。
# print("1234".zfill(3))
# 
# 
