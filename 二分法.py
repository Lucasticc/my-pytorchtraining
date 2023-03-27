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
            # 当目标大于mid时使用mid加一作为新的left
            left = mid+1
    return left
print(seacher(1,[3,4,5,6,78]))