class solution:
    def trap(self,height):
        left = 0
        sum = 0
        water_eval= 0
        while left < len(height) - 1:
            right = left + 1
            water_eval = height[left]
            while height[right] < height[left]:
                right += 1
                if right > len(height) - 1:
                    right = left + 1
                    for i in range(left + 1, len(height)):
                        if height[i] > height[right]:
                            right = i
                    water_eval = height[right]
                    break

            for i in range(left,right):
                sum += water_eval - height[i]
            left = right   
        return sum

height = list(map(int,input().split()))
sum = solution().trap(height)
print(sum)