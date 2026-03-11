name = '丁真'
gender =  '妈妈'
weight = 65.6
age = 20
#字符串只能与字符串相拼接，拼其他类型会报错
info = "我叫"+name+"我是"+gender+"生的"
print(info)
"""占位符
        %s：占位字符串  
        %f:占位浮点型  
        %i:占位整形  
        %d：占位十进制的整数，单词是：decimal"""
info2 = '我叫%s,我是%s生的，我的体重是%f,年龄是%i'%(name,gender,weight,age)
print(info2)
#其他类型可以转字符串，但是字符串不能转其他类型
info3 = '我叫%s,我是%s生的，我的体重是%s,年龄是%s'%(name,gender,weight,age)
print(info3)
#f-string 花括号里可直接进行运算
info4 = f'我的名字是{name},我是{gender}生的,我的体重是{weight}，我的年龄{age+2}'
print(info4)
#占位精度控制
"""
%m.ns m:字符串最小宽度，位数不够使用空白自动补齐，正数是右对齐，负数是左对齐
     n:精度控制，最多展示几个字符
%m.nf m:整体宽度(整数+小数点+小数)，位数不够使用空格自动补全，正数是右对其，负数是左对齐
      n:精度控制，保留几位小数，默认保留6位小数
%m.nd m:最小宽度，位数不够空格来补，正数是右对齐，负数是左对齐
      n:精度控制，最小显示数字，位数不够用0补
"""
info5 = '5我叫%-5.2s,我是%3.1s生的，我的体重是%-6.2f,年龄是%4.5d'%(name,gender,weight,age)
print(info5)
