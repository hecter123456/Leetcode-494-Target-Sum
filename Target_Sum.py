import unittest

class unitest(unittest.TestCase):
    def testEmptylist(self):
        nums = []
        S = 0
        self.assertEqual(Solution().findTargetSumWays(nums,S),0)
    def testSampleCase(self):
        nums = [1,1,1,1,1]
        S = 3
        self.assertEqual(Solution().findTargetSumWays(nums,S),5)

class Solution():
    def findTargetSumWays(self, nums, S):
        ans = 0
        if nums == []:
            return ans
        queue = [0,'E']
        i = 0
        for node in queue:
            if i == len(nums):
                if node == S:
                    ans += 1
                continue
            if node == 'E':
                i += 1
                queue += 'E'
            else:
                queue += ((node + nums[i]),(node - nums[i]))
        return ans

if __name__ == '__main__':
    unittest.main()
