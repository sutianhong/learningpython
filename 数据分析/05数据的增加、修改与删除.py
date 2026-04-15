#增加数据
##按列增加
df['name']=[88,76,66,54]    #name不在数据中
df.loc[:,'name'] = [88,76,66,54]
df.insert(1,'name',[88,76,66,54])   #在指定位置插入一列
##按行增加数据
df.loc['name']=[12,44,66]
###增加多行数据
df_insert=pd.DataFrame({'one':[11,33,44],'two':[11,22,33]})
df1=df.append(df_insert)


#修改数据
##修改列标题
df.columns=['one','two','three']    
df.rename(columns={'one'='one','two'='two','three'='three'})
##修改行标题(axis=0时操作行,inplace=false时返回新副本)
df.index=list('1234')
df.rename({'明日':1,'七月流火':2,'高袁圆':3,'二月二':4},axis=0,inplace = True)
###修改数据
####修改整行数据
df.loc['name']=[11,23,5,65]
####修改整列数据
df.loc[:,'name']=[23,43,54,76]
####修改某一数据
df.loc['name1','name2']=13
####使用iloc修改数据
df.iloc[0,0]=34



#删除数据
DataFrame.drop()
##删除行列数据
###行
df.drop(index=['行标签1', '行标签2'], inplace=True)
df.drop(df.index[[0, 2]], inplace=True)  # 按位置删除
###列
df.drop(columns=['列名1', '列名2'], inplace=True)
df.drop('列名', axis=1, inplace=True)
##删除特定条件的行
df.drop(index=df[df['语文']<110].index[0],inplace=True)