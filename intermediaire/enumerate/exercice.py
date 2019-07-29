phrase = 'Phrase en camel case'
words = phrase.lower().split(' ')
phrase_finale = words[0]
for i, word in enumerate(words):
    if i > 0:
        phrase_finale += word.capitalize()
print(phrase_finale)

# Convertir la phrase ci-dessus dans ce format :
'phraseEnCamelCase'