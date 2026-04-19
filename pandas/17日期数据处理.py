#dataframe的日期数据转换
pandas.to_datetime(arg,errors='ignore',dayfirst=False,yearfirst=False,utc=None,box=True,form=True,unit=None,infer_datetime_format=False,origin='unix',cache=False)

#dt对象的使用
Series.dt() #获取日期属性

##获取年月日
df['年'],df['月'],df['日']=df['日期'].dt.year,df['日期'].dt.month,df['日期'].dt.day
##从日期判断出所处星期数
df['星期几']=df['日期'].dt.day_name()
##从日期判断所处季度
df['季度']=df['日期'].dt.quarter
##从日期判断是否为年底最后一天
df['是否年底']=df['日期'].dt.is_year_end


#获取日期区间数据
##获取2018年的数据。
df1['2018']
##获取2017—2018年的数据。
df1['2017':'2018']
##获取某月（2018年7月）的数据。
df1['2018-07']
##获取具体某天（2018年5月6日）的数据。
df1['2018-05-06':'2018-05-06']


#按不同时期统计并显示数据

##按时期统计数据
###按年统计数据
df1=df1.resample('AS').sum()
###按季度统计数据
df2.resample('Q').sum()
###按月度统计数据
df1.resample('M').sum()
###按星期统计数据
df1.resample('W').sum()
###按天统计数据
df1.resample('D').sum()

##按时期显示数据
df.to_period(freq,axis,copy)

##按时期统计并显示数据
###按年统计并显示数据
df2.resample('AS').sum().to_period('A')
###按季度统计并显示数据
Q_df=df2.resample('Q').sum().to_period('Q')
###按月统计并显示数据
df2.resample('M').sum().to_period('M')
###按星期统计并显示数据（前5条数据）
df2.resample('W').sum().to_period('W').head()



