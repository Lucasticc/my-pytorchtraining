def de(nums,target):
    l = len(nums)
    right,left = l,0
    while left<right:
        mid = left +(right - left)//2
        if target<nums[mid]:
            right = mid
        else:
            left = mid+1
    return right-1
# de = de()
print(de([1,2,3,4,5],6))

