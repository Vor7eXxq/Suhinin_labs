def count_vovels(text):
    count = 0
    for char in text:
        if char.lower() in "ауеєіоиїюяaeiou":
            count += 1
    return count

def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(word for word in words)

def pig_latin(text):
    words = text.split()
    pig_latin_words = []
    for word in words:
        if len(word) > 1:
            new_word = word[1:] + word[0] + "ay"
            pig_latin_words.append(new_word)
        else:
            pig_latin_words.append(word + "ay")
    return " ".join(pig_latin_words)
