#创建DataFrame对象(index:行索引，columns:列索引，dtype:数据的数据类型，copy:用于复制数据)
pandas.DataFrame(data,index,columns,dtape,copy)
#通过二维数组创建DataFrame
df=pd.DataFrame(data='二维数组',columns=columns)
#通过字典创建DataFrame
df=pd.DataFrame(data='字典',columns=columns)
