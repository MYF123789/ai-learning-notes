class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_num = {0:1}
        for i in nums:
            prefix_sum = prefix_sum + i
            need = prefix_sum - k
            count += prefix_num.get(need,0)
            prefix_num[prefix_sum] = prefix_num.get(prefix_sum, 0) + 1
    

        return count


s = Solution()
nums = list(map(int,input().split(",")))
k = int(input())
count = s.subarraySum(nums,k)
print(count)
            