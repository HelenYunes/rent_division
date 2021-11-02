
from typing import List
from agent import OrdinalAgent

def findAlmostEnvyFree1(agents: List[OrdinalAgent], prices: list[int]):
    n = len(agents)
    roomAndAgent = dict()
    for i in range(n):
        roomForAgentI=agents[i].bestRoom(prices)
        if roomAndAgent.get(roomForAgentI) == None:
            roomAndAgent[roomForAgentI] = agents[i]
        else:
            return None 
    return roomAndAgent

def findAlmostEnvyFree(agents: List[OrdinalAgent], totalRent: int):
    for price1 in range(0,totalRent+1): 
        for price2 in range(0,totalRent-price1+1):
            price3=totalRent-price1-price2
            prices=[price1,price2,price3]
            envyFreeDivision=findAlmostEnvyFree1(agents,prices)
            if (envyFreeDivision!=None):
                agent0 = agents[0].bestRoom(prices)
                agent1 = agents[1].bestRoom(prices)
                agent2 = agents[2].bestRoom(prices)
                if agent0 != agent1 and agent0 != agent2 and agent1 != agent2:
                 print(f'Agent 0 receives room {agent0} for {prices[agent0]} shekels.')
                 print(f'Agent 1 receives room {agent1} for {prices[agent1]} shekels.')
                 print(f'Agent 2 receives room {agent2} for {prices[agent2]} shekels.')
                 return
                else:
                    pass
                     
def main ():
    a = OrdinalAgent()
    b = OrdinalAgent()
    c = OrdinalAgent()
    findAlmostEnvyFree([a,b,c],100)
if __name__ == '__main__':
    main()











