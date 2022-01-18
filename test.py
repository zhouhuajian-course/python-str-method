"""


@author  : zhouhuajian
@version : v1.0
"""

print("thIS iS a teST".capitalize())
print("thIS iS a teST".title())

print("ß".casefold())
print("ß".lower())

print('---')
print("1234".isdecimal())  # 普通数字
print("１２３４".isdecimal())  # 全角数字
print("¹²³⁴".isdecimal())  # 上标数字
print("₁₂₃₄".isdecimal())  # 下标数字
print("①②③④".isdecimal())  # 圆圈数字
print("一二三四".isdecimal())  # 汉字数字
print("ⅠⅡⅢⅣ".isdecimal())  # 罗马数字

print('---')
print("1234".isdigit())  # 普通数字
print("１２３４".isdigit())  # 全角数字
print("¹²³⁴".isdigit())  # 上标数字
print("₁₂₃₄".isdigit())  # 下标数字
print("①②③④".isdigit())  # 圆圈数字
print("一二三四".isdigit())  # 汉字数字
print("ⅠⅡⅢⅣ".isdigit())  # 罗马数字

print('---')
print("1234".isnumeric())  # 普通数字
print("１２３４".isnumeric())  # 全角数字
print("¹²³⁴".isnumeric())  # 上标数字
print("₁₂₃₄".isnumeric())  # 下标数字
print("①②③④".isnumeric())  # 圆圈数字
print("一二三四".isnumeric())  # 汉字数字
print("ⅠⅡⅢⅣ".isnumeric())  # 罗马数字