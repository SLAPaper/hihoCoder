from __future__ import print_function

_ = raw_input()
words = [set(w) for w in raw_input().split()]

result = 0


def search(words, layer=0):
    global result

    if len(words) + layer <= result:
        # simple cut
        return

    if layer > result:
        result = layer

    def isConflict(word1, word2):
        return any(c1 in word2 for c1 in word1)

    for i in range(len(words)):
        nw = [w for w in words[i + 1:] if not isConflict(words[i], w)]
        search(nw, layer + 1)


search(words)
print(result)
