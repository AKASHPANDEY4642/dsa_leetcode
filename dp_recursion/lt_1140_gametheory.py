class Solution:
    def solveForAlice(self, piles, person, i, M, n, t):
        if i >= n:
            return 0
        
        if t[person][i][M] is not None:
            return t[person][i][M]
        
        if person == 1: 
            result = -1
        else:            
            result = float('inf')
        
        stones = 0
        
        for x in range(1, min(2 * M, n - i) + 1):
            stones += piles[i + x - 1]
            
            if person == 1:
                result = max(result, stones + self.solveForAlice(piles, 0, i + x, max(M, x), n, t))
            else:  
                result = min(result, self.solveForAlice(piles, 1, i + x, max(M, x), n, t))
        
        t[person][i][M] = result
        return result
    
    def stoneGameII(self, piles):
        n = len(piles)
        t = [[[None] * 101 for _ in range(101)] for _ in range(2)]
        return self.solveForAlice(piles, 1, 0, 1, n, t)

       
