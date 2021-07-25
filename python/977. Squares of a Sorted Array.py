"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    """
    直接排序
    时间复杂的: O(nlog n)
    空间复杂的: O(log n), 栈空间进行排序
    """
    def sortedSquares_direct(self, nums: List[int]) -> List[int]:
        return sorted(num*num for num in nums)

    
    """
    双指针
    方法一没有利用 nums 已经按照升序排序这个条件。显然，如果 nums 中的所有数都是非负数，那么将每个数平方后，数组仍然保持升序；
    如果 nums 中的所有数都是负数，那么将每个数平方后，数组会保持降序。

    这样一来，如果我们能够找到 nums 中负数与非负数的分界线，那么就可以用类似「归并排序」的方法了。
    具体地，我们设 neg 为数组 nums 中负数与非负数的分界线，也就是说，nums[0] 到 nums[neg] 均为负数，而 nums[neg+1] 到 nums[n−1] 均为非负数。
    当我们将数组 nums 中的数平方后，那么 nums[0] 到 nums[neg] 单调递减，nums[neg+1] 到 nums[n−1] 单调递增。

    由于我们得到了两个已经有序的子数组，因此就可以使用归并的方法进行排序了。具体地，使用两个指针分别指向位置 neg 和 neg+1，
    每次比较两个指针对应的数，选择较小的那个放入答案并移动指针。当某一指针移至边界时，将另一指针还未遍历到的数依次放入答案。
    
    时间复杂的: O(n)
    空间复杂的: O(1)
    """
    def sortedSquares_pivot2edge(self, nums):
        n = len(nums)
        negative = -1
        for i, num in enumerate(nums):
            if num < 0:
                negative = i
            else:
                break
        
        ans = list()
        i, j = negative, negative + 1
        
        while i >= 0 or j < n:
            if i < 0:   # 负数已经计算完成
                ans.append(nums[j] * nums[j])
                j += 1
            elif j == n:  # 正数已经计算完成
                ans.append(nums[j] * nums[j])
            elif nums[i] * nums[i] < nums[j] * nums[j]:
                ans.append(nums[i] * nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1
            
        return ans

    """
    双指针
    同样地，我们可以使用两个指针分别指向位置 0 和 n−1，每次比较两个指针对应的数，选择较大的那个逆序放入答案并移动指针。
    这种方法无需处理某一指针移动至边界的情况，读者可以仔细思考其精髓所在。

    时间复杂的: O(n)
    空间复杂的: O(1)
    """
    def sortedSquares_edge2pivot(self, nums):
        n = len(nums)
        ans = [0] * n 

        i, j, pos = 0, n-1, n-1

        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                ans[pos] = nums[i] * nums[i]
                i += 1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1
        
        return ans






    


nums = [-7,-3,2,3,11]
s = Solution()


print(s.sortedSquares_direct(nums))
print(s.sortedSquares_pivot2edge(nums))
print(s.sortedSquares_edge2pivot(nums))




