#Word Frequency Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

for words, count in word_counts.items():
    if count > 1:
        print(word,count)
        