class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0

        while(index<len(nums)):
            if target<=nums[index]:
                return index
            index += 1

        return index