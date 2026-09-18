# Given a list of cricket scores [45, 78, 102, 34, 67, 89], use a
# while loop to print each score until you reach a score above 
# 100, then stop printing.

cricket_scores = [45, 78, 102, 34, 67, 89]
i=0

while i < len(cricket_scores):    
    if cricket_scores[i] > 100:
        break
    
    print(cricket_scores[i])
    i=i+1