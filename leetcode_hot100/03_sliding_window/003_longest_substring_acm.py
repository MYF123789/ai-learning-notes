class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = set()
        longest = 0
        left = 0
        for right,word in enumerate(s):
            while word in mp:
                mp.remove(s[left])
                left += 1
            mp.add(word)
            longest = max(longest,right - left + 1)
        return longest

if __name__ == "__main__":
    s = input().strip()
    result = Solution().lengthOfLongestSubstring(s)
    print(result)
