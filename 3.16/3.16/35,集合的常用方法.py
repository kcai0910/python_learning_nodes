a1 = {10,20,30,40,50}
a2 = {30,40,50,60,70}
#在集合a2里，不同于a1的数据
# res = a2.difference(a1)
# print(res)
# print(a1)
# print(a2)
# # #在集合a1里删除集合a2存在的数据(a1原数据会发生变化，a2不会)
# a1.difference_update(a2)
# print(a1)
# print(a2)
# #合并两个集合，并且自动去重，返回一个新的集合，集合a1和集合a2不会变化
# res = a1.union(a2)
# print(a1)
# print(a2)
# print(res)


# a3 = {10,20,30,40,50}
# a4 = {30,40,50,60,70}
# a5 = {30,40,50}
# a6 = {80,90}
# # 判断a5是否为a3的子集,返回bool
# # res = a5.issubset(a3)
# # print(res)
# # #判断a4是否为a5的超集，返回bool
# # res = a4.issuperset(a5)
# # print(res)
# #判断a3与a4是否没有交集,返回bool.只要有一个公共的就返回False
# res = a3.isdisjoint(a4)
# print(res)    