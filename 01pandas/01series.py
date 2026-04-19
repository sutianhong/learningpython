#创建Series对象
s = pd.Series(data,index=index)

eg:
    s = pd.Series([1,2,3],index = [1,2,3])

#输出Series位置索引
s = pd.Series([1,2,3])
print(s[0])
#输出Series标签索引
s = pd.Series([1,2,3],index = ['one','two','three'])
print(s['one'])
#输出Series切片索引
s = pd.Series([1,2,3])
print(s[0:1])

#获取Series索引和值
print(s.index)
print(s.value)
