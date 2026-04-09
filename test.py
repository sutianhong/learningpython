import pandas as pd 
#打开文件
file_path_ob = open("data.csv") 
#读取文件信息
file_data_bjinfo = pd.read_csv(file_path_ob)
#读取的信息
file_data_bjinfo
 
#检测是否有重复数据
file_data_bjinfo.duplicated()
#删除重复数据
file_data_bjinfo = file_data_bjinfo.drop_duplicated()
#去除重复数据后的是数据
file_data_bjinfo

#检测是否存在缺失值
file_data_bjinfo.isnull()

#计算常驻人口的平均数，设置为float类型并保留两位小数
population = float(":.2f".format(
    file_data_bjinfo['常驻人口（万人）'].mean()
))
#以字符映射的形式将需要填充的数据进行对应
value = {'常住人口（万人）':population}
file_data_bjinfo = file_data_bjinfo.fillna(value = vaalues )
file_data_bjinfo

#异常值的检测
file_data_bjinfo.boxplot(column=['行政面积','户籍人口','男性','女性','GDP','常住人口'])

#对两组数据进行合并
pd.concat([file_data_bjinfo,file_data_tjinfo],ignore_index=True)



