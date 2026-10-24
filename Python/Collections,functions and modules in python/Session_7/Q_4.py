text = "the food is good and the delivery is fast"

stopwords = ["the", "and", "in", "of", "a", "to", "is"]

text = text.lower()

for char in ",.!?":
    text = text.replace(char, "")

words = text.split()
result = {}

for word in words:
    if word not in stopwords:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

print(result)