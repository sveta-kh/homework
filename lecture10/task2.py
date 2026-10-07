#Process student scores

scores = [45, 82, 67, 38, 90, 55, 72]

passing_score = list(filter(lambda scores: scores >= 50, scores))
final_score = list(map(lambda score: score + 5 if score <= 95 else 100, passing_score))

print(final_score)

