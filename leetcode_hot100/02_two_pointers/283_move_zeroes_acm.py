class solution:
    def move_zeros(self,nums):
        fast = 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 :
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow,len(nums)):
            nums[i] = 0
        return nums

s = solution()
nums = list(map(int,input().split()))


ans = s.move_zeros(nums)
print(ans)

