class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        sm = sum(arr)
        mx, currSum = 0, 0
        pref, suff = -float("inf"), -float("inf")
        prefCurrSum, suffCurrSum = 0, 0
		
        for x in arr:
            currSum += x
            prefCurrSum += x
            if currSum < 0:
                currSum = 0
            mx = max(mx, currSum) # Kandanes algo
            pref = max(pref, prefCurrSum) # store max prefix sum
			
        for x in arr[::-1]:
            suffCurrSum += x
            suff = max(suff, suffCurrSum) # store max suffix sum
			
        if k != 1:
            mx = max(mx, pref + suff, suff + (sm * (k - 1)), suff + (sm * (k - 2)) + pref)  # order of cases 1, 2, 3, 4
        return mx % ((10 ** 9) + 7)
        