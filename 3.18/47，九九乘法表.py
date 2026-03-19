
# print('心智',end='\n')
# print('悟空',end='')

#九九乘法表
# for i in range(10):
#     print(i,end='\t')
#     for j in range(9):
#         if i==0:
#             print(j+1,end='\t')
#         else:
#             res = (i)*(j+1)
#             print(res,end='\t')
#     print()

for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print('')