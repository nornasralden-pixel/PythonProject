from dataclasses import replace
from typing import final

# date = "28-nov-2025"
# => nov-28-2025

date = "28-nov-2025"
index1 = date.index("-")

# day = date[:2]
day_1 = date[:index1]


index2 = len(date)-4
month= date[index1+1:index2]
final_date = f"{month}{day_1}-2025"
print(final_date)





