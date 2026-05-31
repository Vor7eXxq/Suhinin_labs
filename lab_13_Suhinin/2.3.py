from collections import Counter
def analyze_text(text, n):
    words = [
        word.strip(".,!?;:").lower()
        for word in text.split()
    ]
    counter = Counter(words)
    return counter.most_common(n)
text = "Привіт, світ! Світ прекрасний. Привіт усім!"
print(analyze_text(text, 2))