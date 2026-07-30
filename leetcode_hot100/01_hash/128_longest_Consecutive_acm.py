class solution:
    def longestConsecutive(self,nums):
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            current_length = 1
            current_num = num

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

        return longest

nums = list(map(int,input().split()))
longest = solution().longestConsecutive(nums)
print(longest)
