"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-bad-version
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


class Solution:
    def __init__(self, bad):
        self.bad = bad

    def isBadVersion(self, n):
        if n >= self.bad:
            return True
        else:
            return False


    """
    时间复杂的: O(log n)
    空间复杂度: O(1)
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        
        while left < right:                         # 循环直至区间左右端点相同
            mid = left + (right-left)//2
            if self.isBadVersion(mid) == True:      # 答案在区间 [left, mid] 中
                right = mid 
            else:
                left = mid + 1                      # 答案在区间 [mid+1, right] 中
        
        return left                                 # 此时有 left == right，区间缩为一个点，即为答案



n = 5
bad = 3
s = Solution(bad)

print(s.firstBadVersion(n))

