alfavit = {'1': {'.', ',' '-'},
     '2': {'а', 'б', 'в', 'г'},
     '3': {'д', 'e', 'ж', 'з'},
     '4': {'и', 'й', 'к', 'л'},
     '5': {'м', 'н', 'о', 'п'},
     '6': {'р', 'с', 'т', 'у'},
     '7': {'ф', 'х', 'ц', 'ч'},
     '8': {'ш', 'щ', 'ъ', 'ы'},
     '9': {'ь', 'э', 'ю', 'я'}}

text = input().split()
numbers = input()
for x in text:
    if len(x) >= len(numbers) and \
            all([x[i].lower() in alfavit[j] for i, j in enumerate(numbers)]):
        print(x, end=' ')
