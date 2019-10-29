# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9
# Because nums[0] + nums[1] = 2 + 7 = 9
# return [0, 1]

class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        self.found = False

    def twoSum(self):
        chosen_index = 0
        second_index = None
        
        while(not self.found):
            for index, num in enumerate(self.nums, 0):
                if chosen_index != index:
                    second_index = index
                    
                    if(self.nums[chosen_index] + self.nums[second_index]) == self.target:
                        self.found = True
                        break
            else:
                chosen_index = chosen_index + 1
                continue
            break
        return chosen_index, second_index

s = Solution([3, 4, 5, 1, 9, 17, 98], 99)
q, w = s.twoSum() # 3, 6

s = Solution([3, 4, 5, 1, 9, 17, 98], 115)
q, w = s.twoSum() # 5, 6