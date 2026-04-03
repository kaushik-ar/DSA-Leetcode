class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        n = len(height)
        pre = [0]*n
        post = [0]*n
        water = 0

        pre[0] = height[0]
        post[-1] = height[-1]
        for i in range(0,n):
            pre[i] = max(pre[i-1],height[i])

        for i in range(n-2, -1, -1):
            post[i] = max(post[i+1],height[i])

        for i in range(n):
            water += min(pre[i], post[i]) - height[i]
        return water


        
        
























        # if not height:
        #     return 0
        # n = len(height)
        # pre = [0]*n
        # post = [0]*n
        # water = 0
        # pre[0] = height[0]
        # post[n-1] = height[n-1]

        # for i in range(0,n):
        #     pre[i] = max(pre[i-1], height[i])
        # for i in range(n-2,-1,-1):
        #     post[i] = max(post[i+1], height[i])

        # for i in range(n):
        #     water += min(pre[i],post[i]) - height[i]
        # return water