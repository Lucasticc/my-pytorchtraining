#判断一个数 是否为质数
#规定1既不是质数也不是合数
def judge(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
print(judge(3))