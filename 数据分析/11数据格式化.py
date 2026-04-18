#设置小数位数(decimals小数位数)
df.round(decimals)
df.applymap(lambda x:'%.2f'%x)
#设置百分比
df[''].apply(lambda x:format(x,'.0%'))
df[''].map(lambda x:'{:.0%}'.format(x))
#设置千位分隔符
df[''].apply(lambda x:format(int(x),','))