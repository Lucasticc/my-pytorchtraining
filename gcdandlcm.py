#最小公约数
def gcd(a,b):
    while b:
        #一直往下取余
        a,b=b,a%b
    return a
w=gcd(20,10)
print(w)
#最小公倍数
def lcm(a,b):
    t = a*b
    while b:
        #找到最小公约数就可以用它俩的乘积整除最小公约数 就得到了最小公倍数
        a,b = b,a%b
    return t//a
print(lcm(5,7))
#求n个数字的 最大公约数 使用递归思想
def supergcd(nums):
    larger = len(nums)
    if larger == 1:
        return nums[0]
    elif larger == 2:
        return gcd(nums[0],nums[1])
    else:
        return gcd(supergcd(nums[:larger//2]),supergcd(nums[larger//2:]))
print(supergcd([6,7,434,564,5234]))