#Word Length Filter 

words = ["python", "generator", "yield", "code", "ai", "developer"]

words_filtered = (word.upper() for word in words if len(word) > 4)

for items in words_filtered:
    print(items)

    
