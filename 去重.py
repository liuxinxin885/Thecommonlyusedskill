# @Time : 2020/7/30 0030 9:26 
# @Author : liuxinxin885
# @File : 去重.py 
# @Software: PyCharm
# 对列表去重
# 循环查找
li = [1,2,3,3,4,2,3,4,5,6,1]
news_li = []
for i in li:
    if i not in news_li:
        news_li.append(i)
print (news_li)
# 使用集合的特性
li1 = [1,4,3,3,4,2,3,4,5,6,1]
new_li1 = list(set(li1))
# .使用itertools模块的grouby方法
import itertools
li2 = [1,4,3,3,4,2,3,4,5,6,1]
li2.sort() # 排序
it = itertools.groupby(li2)
for k, g in it:
    print (k)
# 使用while循环遍历
def quchong(lb):
    for x in lb:
        while lb.count(x)>1:
            del lb[lb.index(x)]
    return lb
li3 = [1,4,3,3,4,2,3,4,5,6,1]
print(quchong(li3))
# 使用keys（）
li4 = [1,0,3,7,7,5]
formatli = list({}.fromkeys(li4).keys())
print (formatli)
# 对数据框去重
# 用unique()对单属性列去重
import pandas as pd
data = {'id':['A','B','C','C','C','A','B','C','A'],'age':[18,20,14,10,50,14,65,14,98]}
data = pd.DataFrame(data)
data.id.unique()
#或者
import numpy as np
np.unique(data.id)
# 用frame.drop_duplicates()对单属性列去重
data.drop_duplicates(['id'])
# 用frame.drop_duplicates()对多属性列去重
data.drop_duplicates(['id','age'])
# 用frame.duplicated()对多属性列去重
isduplicated = data.duplicated(['id','age'],keep='first')
data.loc[~isduplicated,:]
