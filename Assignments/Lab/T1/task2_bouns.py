import random as rn
import math as m

Total_hits = 1000000
Correct_hits = 0
for i in range(Total_hits):
    hitx,hity = rn.uniform(-0.5, 0.5), rn.uniform(-0.5, 0.5)
    if m.sqrt((hitx * hitx) + (hity * hity)) <= 0.5:
        Correct_hits += 1

print(4*Correct_hits/Total_hits)