col = ['Астрахань','Три','4','Вера','Да']
#print (col)
res = []
for i in col:
    if len(i) <= 3:
        res.append(i)
print(res)

"""a = len(col[0])
b = len(col[1])
c = len(col[2])
d = len(col[3])
e = len(col[4])

print(a, b,c ,d, e)
print(type(a), type(b), type(c), type(d), type(e))"""
