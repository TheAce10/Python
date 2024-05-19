# def solution(n=[]):
#     count= 0
#     for i in n:
#         if i[0]== '.':
#             if i[1]== '.':
#                 count-= 1
#         else:
#             count+=1
#     return count

# # print(round(2.6))
# def maxProfit(prices):
#     if len(prices)==1:
#             return 0
#     ind = prices.index(min(prices))
#     l = len(prices)
#     if ind == l-1:
#         ind= prices.index(min(prices[:l-1]))
#         if ind!= l-2:
#             return max(prices[ind:]) -prices[ind]
#         else:
#             return 0
#     elif prices[ind]==0:
#         ind= prices.index(min(prices[:ind]+prices[ind+1:]))
#     else: 
        
#         return max(prices[ind:]) - prices[ind]
                
# print(maxProfit([3,2,6,5,0,3]))
# 
# print(max([1,2,3,4,5]))       
# 


# print(''.join([1,2,3,4,5]))         

x = set("abrss")
print(x)