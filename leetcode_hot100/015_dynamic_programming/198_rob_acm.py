class Solution:
    def rob(self, nums: list[int]) -> int:
        ans = []
        n = len(nums)
        for i,num in enumerate(nums):
            if i == 0:
                ans.append(num)
            elif i == 1:
                ans.append(num)
            elif i == 2:
                ans.append(nums[0]+nums[2])
            else:
                tem = max((ans[i-2]+nums[i]),(ans[i-3]+nums[i]))
                ans.append(tem)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        else:
            return max(ans[n-1],ans[n-2])

if _main_:
    s = Solution()
    nums = list(map(int,input().split()))
    ans = s.rob(nums)
    print(ans)