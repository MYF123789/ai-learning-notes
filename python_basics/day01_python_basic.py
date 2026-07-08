class solution:
    def two_sum(self,nums,target):
        table = {}

        for i,num in enumerate(nums):
            need = target - num

            if need in table:
                return table[need],i
            
            table[num] = i
        return -1,-1
    
n = int(input())
nums = list(map(int,input().split()))
target = int(input())

s = solution()
i,j = s.two_sum(nums,target)
print(i,j)