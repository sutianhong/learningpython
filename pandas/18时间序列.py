#重采样(resample()方法)
DataFrame.resample(rule,how=None,axis=0,fill_method=None,closed=None,label=None,convention=None,loffset=None,limit=None,base=0,on=None,level=None)

#降采样处理
df.resample('W').sum().head()

#升采样处理
##不填充
df.resample('').asfreq()
##用前值填充
df.resample('').ffill()
df.resample('').pad()
##用后值填充
df.resample('').bfill()

#时间序列数据汇总
series.resample.ohlc()

#移动窗口数据计算
DataFrame.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=left)


