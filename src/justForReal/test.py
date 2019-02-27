wordList = ["hot","dot","dog","lot","log","cog"]


def construct_dict(word_list):
    d = {}
    for word in word_list:
        for i in range(len(word)):
            s = word[:i] + "_" + word[i + 1:]
            d[s] = d.get(s, []) + [word]
    return d
print("hot"[1:])
print(construct_dict(wordList))