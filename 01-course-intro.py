"""
第01课 课程介绍 演示6个字符串方法

@author  : zhouhuajian
@version : v1.0
"""

languages = "c,c++,python"
language_list = languages.split(",")
print(language_list)
#
print('-----------')
print(",".join(language_list))
#
print('-----------')
# 实现输出0001 0002 0003
for i in range(1, 4):
    # print(str(i).rjust(4, "0"))
    print(str(i).zfill(4))

print('-----------')
print('========== 开始 ==========')
print(" 开始 ".center(24, "="))

print('-----------')
students = """Name\tGender\tAge
Jack\tmale\t18
Tom\tmale\t6
Lucy\tfemale\t20"""
print(students)
print('-----------')
print(students.expandtabs(tabsize=8))