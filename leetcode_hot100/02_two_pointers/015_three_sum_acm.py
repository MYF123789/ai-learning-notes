class solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            # i=0 时不能比较 nums[i-1]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                current = nums[left] + nums[right]

                if current > target:
                    right -= 1

                elif current < target:
                    left += 1

                else:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # 找到答案后才去重
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans


s = solution()
nums = list(map(int,input().split()))
mp = s.threeSum(nums)
print(mp)