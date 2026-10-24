review = """zomato food is good
zomato delivery is fast
food is good"""

review = review.lower()

for char in ",.!?":
    review = review.replace(char, "")

words = review.split()

result = {}

for word in words:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)