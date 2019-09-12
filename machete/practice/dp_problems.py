from typing import List
from collections import defaultdict
import numpy as np

def dp_min_coins_count(denoms:List[int], N:int) -> int:
    """Given an array of denominations of coins "denoms" and target amount "N", calculate
    minimum possible number of coins used."""
    # [1,2,5] 
    # 11
    #base cases
    dp = np.full((N+1,), np.inf)
    # print(np.isposinf(dp))
    dp[0] = 0
    for i in range(1,N+1):
        for x in denoms:
            # print('{} {}'.format(dp[i], dp[i-x]))
            dp[i] = min(dp[i], dp[i-x]+1)
            # print('{} : {}'.format(i, dp[i]))
    print(dp[N])



if __name__ == "__main__":
    dp_min_coins_count([1,2,5], 11)    