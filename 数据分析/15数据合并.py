#merge方法
pandas.merge()


##常规合并
df_merge=pd.merge(df1,df2,right_index,left_index)
##多对一数据合并
df_merge=pd.merge(df1,df2,on)
##多对多数据合并
df_merge=pd.merge(df1,df2)


#concat方法
pandas.cancat()

##相同字段的表首尾相接
result = pd.concat(dfs,key)

##横向表合并（行对齐）
result = pd.concat([df1, df4], axis=1)

#交叉合并
result = pd.concat([df1, df4], axis=1, join='inner')

#指定表对齐数据（行对齐）
result = pd.concat([df1, df4], axis=1, join_axes=[df4.index])



