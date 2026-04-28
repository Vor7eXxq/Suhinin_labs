import text_processor
text = input("Введіть текст: ")
print(f"Голосних: {text_processor.count_vovels(text)}\nЗворотній порядок слів: {text_processor.reverse_words(text)}\nПіг-латин: {text_processor.pig_latin(text)}")
