import unittest

class unitest(unittest.TestCase):
    def testEmptylist(self):
        nums = []
        S = 0
        self.assertEqual(Solution().findTargetSumWays(nums,S),0);

class Solution():
    def findTargetSumWays(self, nums, S):
        ans = 0
        return ans

if __name__ == '__main__':
    unittest.main()
