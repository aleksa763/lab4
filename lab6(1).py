d = {'house': 'дом', 'river': 'река', 'car': 'машина', 'tree': 'дерево', 'book': 'книга'}
text = input("Введите строку с английскими словами: ")
words = text.split()
translated_words = []

for word in words:
    if word in d:
        translated_words.append(d[word])
    else:
        translated_words.append(word)

result = ' '.join(translated_words)
print(result)
