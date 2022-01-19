from collections import defaultdict


def get_unique_list(anagram_list, word):
    if anagram_list.count(word) == 0:
        anagram_list.append(word)
    return anagram_list


def is_anagrams(words):
    anagrams_set = map(lambda word: ''.join(sorted(word.lower())), words)
    if len(set(anagrams_set)) == 1:
        return True
    return False


def get_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        anagram_dict[str(sorted(word.lower()))] = get_unique_list(anagram_dict[str(sorted(word.lower()))], word)
    result = []
    for value in anagram_dict.values():
        if len(value) > 1:
            if is_anagrams(value):
                result.append(value)
    return result


def main():
    file = open('sentence.txt', 'r')
    sentence = file.read()
    words = sentence.split(' ')
    anagrams_list = get_anagrams(words)
    print(anagrams_list)


if __name__ == "__main__":
    main()
