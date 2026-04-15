#缺失值查看及处理
##查看
df.info()
df.isnull()
df.notnull()
##处理
###删除
df1=df.dropna()
df2=df[df['宝贝总数量'].notnull()]  #判断特定种类数据是否存在缺失值
###填充
df['name']=df['name'].fillna(333)


#重复值处理
##判断
df.duplicate()
##去除重复数据(keep:保留)
df.drop_duplicate(['name'],keep='last')
##直接删除，保留一个副本
df.drop_duplicate(['name'],inplace=Fasle)   #inplace=True表示直接在原来的DataFrame删除重复项


#异常值的检测与处理
##检测
1.根据给定数据范围判断
2.均方差的2~3 个标准差
3.箱型图的上限与下限
##处理
1.删除
2.以某个值填充
3.当作特殊情况处理
