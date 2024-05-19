ind = prices.index(min(prices))
    l = len(prices)
    if ind == l-1:
        ind= prices.index(min(prices[:l-1]))
        if ind!= l-2:
            return max(prices[ind:]) -prices[ind]
        else:
            return 0
    elif prices[ind]==0:
        ind= prices.index(min(prices[:ind]+prices[ind+1:]))
    else: 
        
        return max(prices[ind:]) - prices[ind]