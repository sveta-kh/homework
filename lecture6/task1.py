#Student Score Manager

scores = []

scores.append (45)
scores.append (88)
scores.append (92)
scores.append (60)
scores.append (75)

scores.remove (45)

average = sum(scores) / len (scores)
highest = max(scores)
lowest = min(scores)

print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

scores.sort()
print(scores)

passed_scores = [score for score in scores if score >= 60]
print(passed_scores)