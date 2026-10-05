#Text Analyzer 

def analyze_text(text, min_length = 3, ignore_stopwords = None):
    if ignore_stopwords is None:
        ignore_stopwords = []

    words = text.split()

    count = 0
    for word in words:
        if len(word) >= min_length and word not in ignore_stopwords:
            count += 1
    return count

text = "Python is a very useful for network automation"

print(analyze_text(text, min_length = 2, ignore_stopwords = ["Python", "network"]))


        
