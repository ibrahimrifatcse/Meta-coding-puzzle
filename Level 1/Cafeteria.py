from typing import List
# Write any import statements here
import math
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
   # Write your code here
    S.sort()
    ES = 0
    FOS = 1
    for i in S:
        openSeats = i - K - FOS
        if openSeats > 0:
            ES += math.ceil(openSeats / (K + 1))
        FOS = i + K + 1
    openSeats = N + 1 - FOS
    if openSeats > 0:
        ES += math.ceil(openSeats / (K + 1))
    return ES
  
