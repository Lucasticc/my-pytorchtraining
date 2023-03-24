#二分法 向数组种插入元素 
# 循环的条件使用
def seacher(target,nums):
    l = len(nums)
    left , right = 0 , l
    while left < right:
        mid = left + (right- left)//2
        if target < nums[mid]:
            right = mid
        else:
            left = mid+1
    return left
print(seacher(9,[3,4,5,6,78]))