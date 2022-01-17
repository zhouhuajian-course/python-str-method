"""
Python 字符串方法 21-30

@author  : zhouhuajian
@version : v1.0
"""

print("-" * 10)
print(" \t\n\r".isspace())
print(" \t\n\rtest".isspace())
print("".isspace())

print("-" * 10)
print("What A Nice Day!".istitle())
print("what A niCe Day!".istitle())
print("".istitle())

print("-" * 10)
print("SUNDAY".isupper())
print("SUNDAY有其他字符".isupper())
print("SuNDAY有其他字符".isupper())
print("其他字符".isupper())

print("-" * 10)
print("".join(["Today", "is", "sunday"]))
print(" ".join(["Today", "is", "sunday"]))
print("---".join(["Today", "is", "sunday"]))
# 如果 iterable 中存在任何非字符串值包括 bytes 对象则会引发 TypeError
# print("---".join([123, "is", "sunday"]))
# print("---".join([b"Today", "is", "sunday"]))

print("-" * 10)
print("t".ljust(4))
print("te".ljust(4))
print("test".ljust(4))
print("t".ljust(4, "*"))
print("te".ljust(4, "*"))
print("test".ljust(4, "*"))

print("-" * 10)
print("XiaoMing".lower())
print("XiaoMing小明".lower())

print("-" * 10)
print(" \t\r\ntest".lstrip())
print("abababctest".lstrip("cba"))

print("-" * 10)
# 如果只有一个参数
translation_table = str.maketrans({
    0x6c49: "这是汉字的汉",
    0x5B57: "这是汉字的字"
})
print(translation_table)
print("汉字".translate(translation_table))

translation_table = str.maketrans({
    "汉": 0x5c0f,
    "字": 0x660e
})
print(translation_table)
print("汉字".translate(translation_table))
print("汉字字汉".translate(translation_table))

translation_table = str.maketrans({
    "汉": None,
    "字": None
})
print(translation_table)
print("这是个汉字，不是其他".translate(translation_table))

# 如果有两个参数
# 65 A 66 B 67 C
# 97 a 98 b 99 c
translation_table = str.maketrans(
    "abcdefg", "ABCDEFG"
)
print(translation_table)
print("test abc".translate(translation_table))

# 如果有第三个参数
translation_table = str.maketrans(
    "abcdefg", "ABCDEFG", "ts "
)
print(translation_table)
print("test abc".translate(translation_table))

print("-" * 10)
print("13:24:18".partition(":"))
print("13:24:18".partition("-"))

print("-" * 10)
print("PythonBook".removeprefix("Python"))
print("PythonBookPython".removeprefix("Python"))
# /表示前面的参数必须传位置参数，不能传关键字参数
# print("PythonBook".removeprefix(prefix="Python"))
