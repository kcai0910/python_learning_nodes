#0 1 2 3 4  5 6 7 8 9 10 十进制
#0 1 10 11 二进制
#0 1 2 3 4 5 6 7 10 八进制
#0 1 2 3 4 5 6 7 8 9 a b c d e f 十六进制

# pink red blue yellowgreen
#255,188,166 rgb 256**3个
#188,177,166,1 rgba
# #27cd66 哈希值 0-9 a-f

#进制转换
# 25 - 11001 #10 -2
# 540 -1034  #10 - 8
#十进制转二进制
print(bin(25))
#十进制转8进制
print(oct(540))
#十进制转16进制
print(hex(463))

num1 = 0b11001 #0b表示二进制 bin
num2 = 0o1034  #0o表示八进制 oct
num3 = 0x1cf   #0x表示十六进制 hex
print(num1,num2,num3)
print(num1+1)

print(int('0b11001',2)) #二进制转十进制
print(int('0o1034',8))  #八进制转十进制
print(int('0x1cf',16))  #十六进制转十进制