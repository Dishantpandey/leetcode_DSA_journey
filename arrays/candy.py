class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        
        candies = 1
        up = 0
        down = 0
        peak = 0
        
        for i in range(1, len(ratings)):
            # Case 1: Increasing slope (Up)
            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                peak = up
                candies += 1 + up
                
            # Case 2: Equal rating (Flat)
            elif ratings[i] == ratings[i - 1]:
                up = 0
                down = 0
                peak = 0
                candies += 1
                
            # Case 3: Decreasing slope (Down)
            else:
                up = 0
                down += 1
                # If down slope length exceeds peak, peak child needs +1 candy
                candies += down + (1 if down > peak else 0)
                
        return candies