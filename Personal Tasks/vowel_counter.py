#create a function that takes a string and returns a dictionary
# showing the count of each vowel (a, e, i, o, u)


def vowel_finder(words):
    storage = {}
    for word in words: 
        if word.lower() in "aeiou":
            word = word.lower()
            storage[word] = storage.get(word, 0) + 1        # storage.keys += word
    return storage
        # storage.values = len(word)
       
name = "pAscaline"
print(vowel_finder(name))
 

