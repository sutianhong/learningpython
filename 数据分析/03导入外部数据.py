#导入.xls与.xlsx文件
df=pd.read_excel('test.xlsx')
##导入指定sheet页
df=pd.read_excel('test.xlsx', sheet_name='sheet1')
##通过行、列索引导入指定行、列数据
df=pd.read_excel('test.xlsx',index_col=0)  #指定 Excel 表格中的第 0 列（即第一列）作为 DataFrame 的索引列
df=pd.read_excel('1月.xlsx',header=1)   #设置第1行为列索引
df=pd.read_excel('1月.xlsx',header=None) #列索引为数字
##导入指定列数据
df=pd.read_excel('1 月.xlsx',usecols=[0]) #导入第1列


#导入.csv文件
df=pd.read_csv('test.csv',encoding='gbk')


#导入.txt文本文件
df=pd.read_csv('test.txt',sep='\t',encoding='gbk')


#导入HTML网页
df=pd.read_html(url)

