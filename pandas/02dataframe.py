#创建DataFrame对象(index:行索引，columns:列索引，dtype:数据的数据类型，copy:用于复制数据)
pandas.DataFrame(data,index,columns,dtape,copy)
#通过二维数组创建DataFrame
df=pd.DataFrame(data='二维数组',columns=columns)
#通过字典创建DataFrame
df=pd.DataFrame(data='字典',columns=columns)


#DataFrame的重要属性
values      值
dtype       类型
index       行名
columns     列名
T           转置
head        前5条数据
tail        后5条数据
shape       查看行数列数
info        查看索引,数据类型和内存信息

#DataFrame的重要函数
describe    统计汇总信息
count       每一列非空值个数 
sum         每一列的和
max         每一列最大值
min         每一列最小值
argmax      最大值的自动索引位置
argmin      最小值的自动索引位置
idxmax      最大值的自定义索引位置
idxmin      最小值的自定义索引位置
mean        每一列平均值
median      每一列中位值
var         每一列方差
std         每一列标准差
isnull      是否有空值
notnull     是否有空值