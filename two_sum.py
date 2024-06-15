# we need to follow one pass solution which is hashmap otherwise brute force could be solution where O(n^2)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}  

        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev_map:
                return [prev_map[complement], i]  
            prev_map[num] = i  # Add current number and index to the map

        # If loop completes without finding a match, return an empty list
        return []
