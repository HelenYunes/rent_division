from typing import List
import random

class OrdinalAgent:
# INPUT: the prices of the n rooms, in shekels.
# OUTPUT: the index of a room that the agent most
# prefers in these prices. Index is between 0 and n-1.
 
     def bestRoom(self, prices:List[int])->int:
         price = random.choice(prices)
         index = prices.index(price)
         for i in range (0,3):
                 if (prices[i]==0):
                     index = i
         return index