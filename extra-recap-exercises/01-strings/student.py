def decode1(word):
    while True:
        index = word.find("A")
        if index < 0:
            break
        word = word[0:index] + "o" + word[index + 1 :]

    return word


def decode2(word):
    return word[::2]


def decode3(word):
    space_index = word.find(" ")
    first_word = word[0:space_index]
    remaining = word[space_index:]

    return first_word[::-1] + remaining


def decode4(word):
    return word[2 : int(len(word) / 2) + 2]


def decode5(sentence):
    words = sentence.split(" ")
    for i in range(len(words)):
        word = words[i]
        word = decode1(word)
        word = decode2(word)
        word = decode4(word)

        words[i] = word

    sentence = decode3(" ".join(words))

    return sentence
