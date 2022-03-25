answer = 0
m, n = input().split()
print(m, n)
m = int(m)
n = int(n)
blocks = input().split()
for i in range(len(blocks)):
    blocks[i] = int(blocks[i])
print(blocks)
shoulders = input().split()
for i in range(len(shoulders)):
    shoulders[i] = int(shoulders[i])
print(shoulders)
blocks = [1, 2, 3]
memory = []
start = 1
place = []
for i in range(len(blocks) - 1):
    if i < start:
        memory.append(blocks[i])
        start += 1
        max_blocks = max(memory)
        r = blocks[i] - max_blocks
        if r < 0:
            continue
        elif r > 0:
            place.append(r)
        for j in range(len(place)):
            place[j] = int(place[j])
        print(place)
shoulders.sort(reverse=True)
place.sort(reverse=True)
for i in range(len(shoulders)):
    for j in range(len(place)):
        counter = 0
        if shoulders[i] <= place[j]:
            shoulders.pop(i)
            place.pop(place[j])
            answer += 1
        if shoulders[i] > place[j]:
            shoulders.pop(i)
            continue
print(answer)
