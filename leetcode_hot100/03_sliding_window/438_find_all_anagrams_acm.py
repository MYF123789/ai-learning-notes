class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        mp = set()
        ans = []
        mp.add(p)
        n = len(p)
        left = 0
        target = sorted(p)
        for right,word in enumerate(s):
            if right < n-1:
                continue
            else:
                if sorted(s[right-n+1:right+1]) == target:
                    ans.append(right-n+1)
                else:
                    continue
        return ans
    

s = input().strip()
p = input().strip()
solution = Solution()
ans = solution.findAnagrams(s,p)
print(ans)
