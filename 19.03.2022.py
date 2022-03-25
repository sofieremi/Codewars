# 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a_new = []
# for i in a:
#     if i < 5:
#         a_new.append(i)
#     else:
#         continue
# print(a_new)

# 2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# common = []
# for i in a:
#     if i in b:
#         common.append(i)
# print(common)

# 3
# time = int(input('enter time(seconds) ->'))
# hh = time // 3600
# mm = (time % 3600) // 60
# print(time % 3600)
# ss = (time % 3600) % 60
# print(hh, ':', mm, ':', ss)

# 4
# a = [561, 245, 33, -43, 17, 342, 200, 547, 304, -51, 561, 42, 391, 237, 688, 444, 324, -72, 172, 576, 624, -5, 305, 687, 292, 84, 179, 334, 10, 624, 607, 365, 660, 466, 564, 193, 124, 236, 31, -77, 121, 383, 455, 218, 686, 72, 666, 360, 180, 672, 626, 373, 89, 33, 405, 338, 564, 419, 4, 242, 450, 581, 281, 379, 245, 133, 380, 486, 166, 446, 345, -44, 203, -29, 515, 29, 122, 260, -99, 574, 646, 369, 77, 528, 522, 693, 642, 436, 276, 430, 687, 424, 287, 354, 58, 195, 246, 263, 108, 121]
# for i in a:
#     if i == 237:
#         break
#     if i % 2 == 0:
#         print(i)

# 5
# a = [1, 1, 2]
# b = [2, 3]
# diff = []
# for i in a:
#     if i in b:
#         continue
#     else:
#         diff.append(i)
# print(diff)

a = 'On the other hand, we denounce with righteous indignation and dislike ' \
    'men who are so beguiled and demoralized by the charms of pleasure of ' \
    'the moment, so blinded by desire, that they cannot foresee the pain and' \
    ' trouble that are bound to ensue; and equal blame belongs to those who fail in ' \
    'their duty through weakness of will, which is the same as saying through shrinking from' \
    ' toil and pain. These cases are perfectly simple and easy to distinguish. In free hour,' \
    ' when our power of choice is untrammelled and when nothing prevents our being able to do' \
    ' what we like best, every pleasure is to be welcomed and every pain avoided. But in certain ' \
    'circumstances and owing to the claims of duty or the obligations of business it will frequently ' \
    'occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always' \
    ' holds in these matters to this principle of selection: he rejects pleasures to secure' \
    ' other greater pleasures, or else he endures pains to avoid worse pains.'
b = a
a = a.split()
print(a)
a = set(a)
max_len = 0
word = ''
for i in a:
    if len(i) > max_len:
        max_len = len(i)
        word = i
print(word)
print(a)
c = {i: b.count(i) for i in a}
print(c)
c = {i: b.count(i) for i in a}
vv = 0
k_max = ''
for k, v in c.items():
    if vv < v:
        vv = v
        k_max = k
print(vv, k_max)