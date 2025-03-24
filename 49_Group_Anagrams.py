'''
Difficulty: Medium
https://leetcode.com/problems/group-anagrams/description/
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dp = defaultdict(list)
        for s in strs:
            tmp = s
            s = ''.join(sorted([c for c in s]))
            dp[s].append(tmp)
            
        return [item for item in dp.values()]