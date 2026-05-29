class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        compared_to_index = 0
        compare_index = 1

        while compare_index<=len(nums)-1:

            if nums[compare_index]== nums[compared_to_index]:
                nums[compare_index] = 101
                compare_index += 1
                count += 1
            else:
                compared_to_index = compare_index
                compare_index += 1
                
        nums.sort()
        return len(nums)-count

            

        