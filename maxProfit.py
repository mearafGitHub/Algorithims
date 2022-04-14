def max_profit(prices):
    buy, sell = 0, 0
    max_prf = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            prf = prices[sell] - prices[buy]
            max_prf = max(max_prf, prf)
        else:
            buy = sell
        sell += 1

    return [max_prf, buy, sell]


print(max_profit([5,1,0,7,9,4]))

def maxProfit(prices):
    max = 0
    min = prices[0]

    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
        if prices[i] - min > max:
            max = prices[i] - min

    return max

