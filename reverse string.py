def reverse_words(text: str) -> str:
    memory = ''
    word = ''
    for i in range(len(text)):
        if text[i] != ' ':
            word += text[i]
        else:
            if word != '':
                memory += word[::-1]
                word = ''
            memory += ' '
        if i == len(text) - 1:
            memory += word[::-1]

    return memory
