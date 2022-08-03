class Solution:
    def compare(self, s1, s2):
        if len(s1) != len(s2) + 1:
            return False
        first = 0
        second = 0
        
        while first < len(s1):
            if second < len(s2) and s1[first] == s2[second]:
                first += 1
                second += 1
            else:
                first += 1
        
        if first == len(s1) and second == len(s2):
            return True
        return False
    
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        dp = [1 for _ in range(n)]
        
        words.sort(key = lambda x: len(x))
        
        maxi = float('-inf')
        for i in range(0, n):
            for prev in range(0, i):
                if self.compare(words[i], words[prev]) and dp[i] < 1 + dp[prev]:
                    dp[i] = 1 + dp[prev]
        
            maxi = max(maxi, dp[i])
        
        return maxi