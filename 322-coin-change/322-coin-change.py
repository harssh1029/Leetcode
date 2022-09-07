class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def getans(coins, target, n, dp):
            if n==0:
                if target%coins[n]==0:
                    return target//coins[n]
                else:
                    return float("inf")
        
            if dp[n][target]!=-1:
                return dp[n][target]
            
        
            nottake = getans(coins, target, n-1, dp)
            take = float("inf")
            if target>=coins[n]:
                take = 1+getans(coins, target-coins[n], n, dp)
        
            dp[n][target] = min(nottake, take)
            return dp[n][target]
        
        
        
        dp=[]
        for i in range(len(coins)+1):
            x=[]
            for i in range(amount+1):
                x.append(-1)
            dp.append(x)
            
        ans = getans(coins, amount, len(coins)-1, dp)
        if ans==float("inf"):
            return -1
        return ans