class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost)+1) #creating an empty array with 0 of length equal to len(cost)

        for i in range(2, len(cost)+1):
            take_one_step = min_cost[i-1] + cost[i-1]
            #cost to reach this step + cost to reach outside array with current cost
            take_two_steps = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(take_one_step, take_two_steps)
            
        return min_cost[-1]
        
        