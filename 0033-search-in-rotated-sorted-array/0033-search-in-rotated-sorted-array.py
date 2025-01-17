class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

'''
    O(log(n)) binary search

[4,5,6,7,0,1,2]

left < mid
    if target >= left and target < mid
        right = mid - 1
    else
        left = mid + 1
else
    if target <= right and target > mid
        left = mid + 1
    else
        right = mid - 1

    
'''