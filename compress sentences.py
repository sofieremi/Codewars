def compress(sentence):
    sentence_split = sentence.upper().split()
    dict = {}
    counter = 0
    answer = ''
    for i in range(len(sentence_split)):
        if sentence_split[i] in dict:
            answer += str(dict.get(sentence_split[i]))
        else:
            dict[sentence_split[i]] = counter
            answer += str(counter)
            counter += 1
    return answer


print(compress('The number 0 is such a strange number Strangely it has zero meaning'))





