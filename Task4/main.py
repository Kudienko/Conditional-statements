def check_s(word, letter):
    s = 0
    for i in word:
     if letter == i:
        s += 1
    if s == 0:
        return True
    else:
        return False
string = input()
word = string[0]
string = string[1:]
mas = []
for letter in string:
    if check_s(word, letter):
        word += letter
    else:
        mas.append(word)
        word = letter
mas.append(word)
print(max(mas, key=len))