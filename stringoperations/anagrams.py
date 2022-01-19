from collections import defaultdict

def anagramList(sentence):
    words = sentence.split(' ')
    dict = defaultdict(list)
    for word in words:
        dict[str(sorted(word.lower()))].append(word)
    result = []
    for value in dict.values():
        if(len(value) > 1):
            result.append(value)
    return result
