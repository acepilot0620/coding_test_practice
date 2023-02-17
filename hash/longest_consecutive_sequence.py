class Solution:
    def longestConsecutive(self, nums: list [int]) -> int:
        longest = 0
        dictionary = {}
        for n in nums:
            dictionary[n] = True

        
        for n in dictionary:
            cnt = 1
            target = n + 1
            while target in dictionary:
                cnt += 1
                target += 1
                longest = max(longest, cnt)

        return longest

sol = Solution()
print(sol.longestConsecutive(nums=[4,5,6,3,14,7,11,12,13]))


