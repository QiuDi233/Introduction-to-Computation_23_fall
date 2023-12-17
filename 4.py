n = int(input())
word_indices = {}

for i in range(n):
    word = input().strip()
    if word not in word_indices:
        word_indices[word] = [i]
    else:
        word_indices[word].append(i)

result = []

for word, indices in sorted(word_indices.items()):
    compressed_indices = [str(indices[0])]
    for j in range(1, len(indices)):
        compressed_indices.append(str(indices[j] - indices[j - 1]))
    result.append(f'{word} : {" ".join(compressed_indices)}')

for line in result:
    print(line)