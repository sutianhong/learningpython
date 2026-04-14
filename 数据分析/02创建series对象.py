#创建Series对象
s = pd.Series(data,index=index)

eg:
    s = pd.Series([1,2,3],index = [1,2,3])

#输出Series位置索引
print(s[2])
