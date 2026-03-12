#0-10幼年
# 10-18为青少年
# 18-30为壮年
# 30-50为中年
# 50往后老年
age = int(input('请输入您的年龄:'))
if age >=50:
    print('你是老登')
elif age >=30:
    print('你是中登')
elif age>=18:
    print('你是状登')
else :
    print('小登,给我坐下')