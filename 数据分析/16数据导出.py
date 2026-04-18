#导出.xlsx文件
df.to_excel('text.xlsx')

#导出位.csv文件
##相对位置
df.to_csv('test.csv')
##绝对位置
df.to_csv('d:/test.csv')
##分隔符
df.to_csv('test.csv',stp='?')
##替换空值
df.to_csv('test.csv',na_rep='NA')
##格式化数据
df.to_csv('test.csv',float_format='%.2f')
##保留某列数据
df.to_csv('test.csv',columns=['name'])
##不保留列名
df.to_csv('test.csv',header=False)
##不保留索引
df.to_csv('test.csv',index=False)

##导出多个sheet
work=pd.ExcelWrite('test.xlsx')
df1.to_excel(work,sheet_name='df3')

