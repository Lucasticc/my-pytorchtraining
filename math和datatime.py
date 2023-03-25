import  math
import datetime
print(math.factorial(3))
d = datetime.date (2023,3,24)
print(d.weekday())
print(d.day)
# 判断日期是否合法
def judge(x,y,z):
    try:
        s=datetime.date(x,y,z)
    except:
        print('日期不合法')
judge(2022,2,200)
#快速生成字典
p=dict((i,0) for i in range(10))
print(p)