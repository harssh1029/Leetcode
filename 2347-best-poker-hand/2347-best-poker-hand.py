class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        first = suits[0]
        flag=True
        for i in range(1, len(suits)):
            if first!=suits[i]:
                flag=False
        if flag:
            return "Flush"
        
        h=collections.defaultdict(int)
        for i in range(len(ranks)):
            h[ranks[i]]+=1
            
            
        newh = dict(sorted(h.items(), key=lambda x:(-x[1])))
        #print(newh)
        for i in newh:
            if newh[i]>=3:
                return "Three of a Kind"
            elif newh[i]>=2:
                return "Pair"
            
        return "High Card"