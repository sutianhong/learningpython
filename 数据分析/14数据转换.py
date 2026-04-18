#一列数据转换为多列数据
series.str.split(pat,n,expand)
df=df.join(df[''].str.aplit(',',expand))

#行列转换
df.stack(level,dropna)
df.unstack(level,fill_values)
df.pivot(index,columns,values)

#df->dict
df.to_dict()

#df->list
df.tolist()

#df->tuples
tuple()

#excel->html
df.to_html('text.heml',header,index)
