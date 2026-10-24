def word_freq_dict(text):
    text = text.lower()

    for char in ",.!?":
        text = text.replace(char, "")

    words = text.split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

print(word_freq_dict(text))