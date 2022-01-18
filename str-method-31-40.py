"""
Python 字符串方法 31-40

@author  : zhouhuajian
@version : v1.0
"""

print("-" * 10)
print("01.png".removesuffix(".png"))
print("01.png".removesuffix(".jpg"))
# /表示前面的参数只能传位置参数
# print("01.png".removesuffix(suffix=".png"))



print("-" * 10)
print("zhangsan zhangsi zhangwu".replace("zhang", "li"))
print("zhangsan zhangsi zhangwu".replace("zhang", "li", 2))

print("-" * 10)
print("zhangsan zhangsi zhangwu".rfind("zhang"))
print("zhangsan zhangsi zhangwu".rfind("zhang", 0, 17))
print("zhangsan zhangsi zhangwu".rfind("zhaoliu"))

print("-" * 10)
print("zhangsan zhangsi zhangwu".rindex("zhang"))
print("zhangsan zhangsi zhangwu".rindex("zhang", 0, 17))
# 找不到 引发ValueError
# print("zhangsan zhangsi zhangwu".rindex("zhaoliu"))


print("-" * 10)
print("test".rjust(6))
print("test".rjust(6, "*"))
print("test".rjust(3))

print("-" * 10)
print("12:30:15".rpartition(":"))
print("12:30:15".rpartition("-"))

print("-" * 10)
print("a  \t\r  b \n  c \t\r\n  d".rsplit())
print("12:30:15".rsplit(":"))
print("12:30:15".rsplit(":", maxsplit=1))

print("-" * 10)
print("test   \r\t\n".rstrip())
print("testababab".rstrip("ab"))


print("-" * 10)
print("12:30:15".split(":"))
print("12:30:15".split(":", maxsplit=1))
print("12::30:15".split(":"))
print("12--30--15".split("--"))
print("".split("--"))

print("a  \t\r  b \n  c \t\r\n  d".split())
print("   a  \t\r  b \n  c \t\r\n  d   ".split())
print("".split())

print("-" * 10)
print("第一行\n第二行\r第三行\r\n第四行\n".splitlines())
print("第一行\n第二行\r第三行\r\n第四行\n".splitlines(keepends=True))
print("第一行\n第二行\r第三行\r\n第四行".splitlines(keepends=True))
# 对比split()
print("第一行\n第二行\n第三行\n第四行\n".split("\n"))
print("第一行\n第二行\n第三行\n第四行\n".splitlines())
print("".split("\n"))
print("".splitlines())
