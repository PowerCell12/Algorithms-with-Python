words = input().split(", ")
target = input()

word_index = {}
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue
    words_count[word] = 1


    try:
        index = 0

        while True:
            index = target.index(word, index)

            if index not in word_index:
                word_index[index] = []

            word_index[index].append(word)

            index += len(word)
    except ValueError:
        continue


def find_all_solutions(index, target, word_index, words_count, allCombinations):

    if index >= len(target):
        print(" ".join(allCombinations))
        return

    if index not in word_index:
        return

    for word in word_index[index]:
        if words_count[word] == 0:
            continue

        words_count[word] -= 1
        allCombinations.append(word)

        find_all_solutions(index + len(word), target, word_index, words_count, allCombinations)

        allCombinations.pop()
        words_count[word] += 1


find_all_solutions(0, target, word_index, words_count, [])
