class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in myMap:
                return [i, myMap[x]]
            myMap[nums[i]] = i
