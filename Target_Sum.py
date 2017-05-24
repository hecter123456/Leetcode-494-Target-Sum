import unittest
from collections import defaultdict

class unitest(unittest.TestCase):
    def testEmptylist(self):
        nums = []
        S = 0
        self.assertEqual(Solution().findTargetSumWays(nums,S),0)
    def testSampleCase(self):
        nums = [1,1,1,1,1]
        S = 3
        self.assertEqual(Solution().findTargetSumWays(nums,S),5)
    def testTLEcase(self):
        nums = [10,9,6,4,19,0,41,30,27,15,14,39,33,7,34,17,24,46,2,46]
        S = 45
        self.assertEqual(Solution().findTargetSumWays(nums,S),6606)

class Solution():
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        Ans = {0:1}
        for node in nums:
            dic = defaultdict(int)
            for key,value in Ans.items():
                dic[key + node] += value
                dic[key - node] += value
            Ans = dic
        return Ans[S]

if __name__ == '__main__':
    unittest.main()
