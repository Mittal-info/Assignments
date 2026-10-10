def reverse_message(message):
    reversed_text = ""

    for char in message:
        reversed_text = char + reversed_text

    return reversed_text


print(reverse_message("Hello WhatsApp"))