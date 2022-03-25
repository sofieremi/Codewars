def solve(s):
    vowels = ['a', 'e', 'o', 'i', 'u']
    vowel_count = 0
    lengths = []
    for i in s:
        if i in vowels:
            vowel_count += 1
        else:
            if vowel_count >= 1:
                lengths.append(vowel_count)
                vowel_count = 0
            else:
                continue
    return max(lengths)


print(solve('codewarriooooors'))


