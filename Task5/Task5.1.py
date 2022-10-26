word = input('Введите: ')
unique = []
unique_numbers = []
for i in range(len(word)):
    if i == word.find(word[i]):
        unique.append(word.count(word[i]))
for elem in unique:
    if not elem in unique_numbers:
        unique_numbers.append(elem)
if len(unique_numbers) > 2:
    print("False")
elif len(unique_numbers) == 1:
    print("True")
else:
    maxVal = max(unique_numbers)
    minVal = min(unique_numbers)
    maxCount = ""
    minCount = ""
    for elem in unique_numbers:
        if elem == maxVal:
            maxCount = "True"
        elif elem == minVal:
            minCount = "True"
    if maxCount == "True" and (maxVal - minVal) == 1:
        print(True)
    elif minCount == "True" and minVal == 1:
        print(True)
    else:
        print(False)