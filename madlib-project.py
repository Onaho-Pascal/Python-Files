# import os
# print(os.listdir())
#the content of the "text.txt" is the same with the content in "story.txt"
with open("text.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

#to identify the required words to be replace in angle brackets
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer


for word in words:
    story = story.replace(word, answers[word])


print(story)
