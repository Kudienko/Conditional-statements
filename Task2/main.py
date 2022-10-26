from collections import Counter

text = str(input('Введите текст для поиска анаграмм.')).lower()

mass = text.split()
mass.sort()

for i, word1 in enumerate(mass):
    for word2 in mass[i + 1:]:
        if (Counter(word1) == Counter(word2)):
            print(word1, word2)