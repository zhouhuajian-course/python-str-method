"""
课程介绍

@author  : zhouhuajian
@version : v1.0
"""

print("-" * 10)
print("张三，李四，王五".split("，"))
print("，".join(["张三", "李四", "王五"]))


print("-" * 10)
print("========== 开始 ==========")
print("输出一些日志")
print("输出一些日志")
print("========== 结束 ==========")


print("-" * 10)
print(" 开始 ".center(24, "="))
print("输出一些日志")
print("输出一些日志")
print(" 结束 ".center(24, "="))


print("-" * 10)
# 000001 000002 000003 000004
for i in range(1, 5):
    print(str(i).zfill(6))
    # 这里用rjust(6, "0")也可以



print("-" * 10)
table = "Name\tGender\tAge\nzhangsan\tmale\t18\nlisi\tfemale\t60\nwangwu\tmale\t6"
print(table)
print("-" * 10)
print(table.expandtabs(tabsize=10))

