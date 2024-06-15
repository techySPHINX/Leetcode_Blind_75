class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        
        for n in nums:
            if n in hashset: # if founds duplicate
                return True
            hashset.add(n)
        return False