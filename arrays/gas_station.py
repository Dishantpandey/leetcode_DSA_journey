class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff
            
            # If current tank goes negative, reset start position
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index if total_tank >= 0 else -1