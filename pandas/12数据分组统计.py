#分组
df.groupby()

##一列分组统计
df.groupby('').sum()

##多列分组统计
df1=df.[['','','']]
df1=df1.groupby(['','']).sum()

##分组并且指定列进行数据运算
df1=df1.groupby('')[''].sum()


##对分组数据进行迭代
for name,group in df.groupby(''):
    print(name)
    print(group)

#聚合
df.groupby('分类').agg(['sum','max'])

#分组统计

##使用字典分组统计
df1=df.groupby(dict1,axis=1).sum

##使用series分组统计
df1=df.groupby(s1,axis=1).sum


