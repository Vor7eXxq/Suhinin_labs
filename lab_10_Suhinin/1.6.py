words = ["cat", "elephant", "dog", "house", "algorithm"]
words_filtered = list(filter(lambda x: len(x) > 4, words))
print(words_filtered)
