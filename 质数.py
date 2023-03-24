#判断一个数 是否为质数
#规定1既不是质数也不是合数
# x**0.5 x开根号
def judge(x):
    for i in range(2,x):
        #int(x**0.5)+1 使用这个 好像可以
        if x%i==0:
            return False
    return True
print(judge(3))