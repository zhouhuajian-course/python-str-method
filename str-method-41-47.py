"""
Python 字符串方法 41-47

@author  : zhouhuajian
@version : v1.0
"""

print("-" * 10)
print("today is sunday".startswith("today"))
print("today is sunday".startswith("sunday"))
print("today is sunday".startswith("sunday", 9))
print("today is sunday".startswith("sunday", 9, 15))


print("-" * 10)
print("  \t\r\ntest   \t\r\n".strip())
print("== a little girl ==".strip("="))
print("== a little girl ==".strip("= "))



print("-" * 10)
print("abcdEFGH".swapcase())
# 请注意 s.swapcase().swapcase() == s 并不一定为真值
print("ß".swapcase())  # 两个大写的SS
print("ß".swapcase().swapcase())  # 两个小写的ss
print("ß".swapcase().swapcase() == "ß")





print("-" * 10)
print("test title method".title())
print("teST tiTLE meTHOD".title())
# 缩写形式与所有格的撇号
print("they're bill's friends from the UK".title())




print("-" * 10)
print("abcd".translate({
    97: "A",
    98: 66,
    99: "CCC",
    100: None
}))
translation_table = str.maketrans({
    "a": "A",
    "b": 66,
    "c": "CCC",
    "d": None
})
print(translation_table)
print("abcd".translate(translation_table))

translation_table = str.maketrans({
    "汉": "这是汉字的汉",
    "字": "这是汉字的字"
})
print(translation_table)
print("汉字".translate(translation_table))



print("-" * 10)
print("abcdefg1234汉字".upper())
print("abcdefg1234汉字".upper().isupper())
# 不区分大小写
print("1234汉字".upper().isupper())




print("-" * 10)
print("123".zfill(6))
print("+123".zfill(6))
print("-123".zfill(6))
# 非数字字符串也可以
# 但zfill一般用于数字字符串
print("test".zfill(6))

