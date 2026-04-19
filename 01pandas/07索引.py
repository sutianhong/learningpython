#重新设置索引
##series
s1.reindex([1,2,4,5,6])
##dataframe
df.reindex(['','',''])  #行索引
df.reindex(columns=['','',''])  #列索引


#设置某列为新的行索引
df1=df.set_index([''])
#数据清洗后重新设置连续的行索引
df1 = df.dropna().reset_index(drop=True)


