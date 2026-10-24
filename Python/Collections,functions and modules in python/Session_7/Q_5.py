def char_count_dict(text):
    result = {}

    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


text = input("Enter a string: ")

result = char_count_dict(text)

for char in sorted(result):
    print(char, ":", result[char])