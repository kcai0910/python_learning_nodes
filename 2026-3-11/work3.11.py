import sys
name = '张三'
age = 20
height = 1.75
rid = 5
sys.set_int_max_str_digits(0)
info = '===== 个人信息卡 =====\n姓名：%-7s数据类型: %-2222.20s\n年龄: %-3d\t\t数据类型: %s \n身高: %0.2f\t数据类型: %s\n出生年份:%d\n半径为%d的圆的面积:%.2f'%(name,type(name),age,type(age),height,type(height),2026-age,rid,3.1415926*rid**2)

print(info.expandtabs(4));
#user_name#蛇形命名法
#userName#小驼峰命名法
#UserName#大驼峰命名法
