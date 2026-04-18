df.sort_values()

#按一列数据排序
df1=df.sort_values(by='',ascending=False)
#按多列数据排序
df1=df.sort_values(by=['',''])
#对统计结果排序
df1=df.groupby(['类别'])['销量'].sum().reset_index()
df2=df1.sort_values(by='销量',ascending=False)
#按行数据排序
df=dfrow.sort_values(by=0,ascending=True,axis=1)

