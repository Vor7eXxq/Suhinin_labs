sentences = ["Python is great", "I love programming"]
longestword = max(len(j) for i in sentences for j in i.split())
print(longestword)