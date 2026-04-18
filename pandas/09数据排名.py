df['']=df[''].rank()


#顺序排名
df['销量'].rank(methon='first',ascending=False)
#平均排名
df['销量'].rank(ascending=False)
#最小值排名
df['销量'].rank(methon='min',ascending=False)
#最大值排名
df['销量'].rank(methon='max',ascending=False)
