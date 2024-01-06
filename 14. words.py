force_words = ['сила', 'прибудет', 'с', 'тобой', 'да']
print(id(force_words))
first = force_words.pop()
last = force_words.pop(0)
force_words.insert(0, first)
force_words.append(last)
print(force_words)
print(id(force_words))
