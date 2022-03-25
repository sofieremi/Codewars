print('write a sentence')
sentence = input()
a = '!'
b = '?'
c = ','
d = '!?'
e = '?!'
if c in sentence:
    print('предложение сложное')
elif d or e in sentence:
    print('предложение вопросительно-восклицательное')
elif a in sentence:
    print('предложение восклицательное')
elif b in sentence:
    print('предложение вопросительное')
elif d in sentence:
    print('предложение вопросительно-восклицательное')
elif a and b not in sentence:
    print('предложение повествовательное')

