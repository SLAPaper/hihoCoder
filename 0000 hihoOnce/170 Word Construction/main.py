from __future__ import print_function, division, absolute_import, unicode_literals

_ = int(raw_input())
words = [set(w) for w in raw_input().split()]

iidx = {}  # letter: [word_indexes]
for i, word in enumerate(words):
    for letter in word:
        if letter in iidx:
            iidx[letter].append(i)
        else:
            iidx[letter] = [i]

result = 0


def search(iidx, layer, words=words):
    global result

    if len(iidx) + layer <= result:
        # A* cut
        return

    if layer > result:
        result = layer

    for letter, words_i in iidx.iteritems():
        for word_i in words_i:
            conflict = set()
            for letter in words[word_i]:
                conflict.update(iidx[letter])

            new_iidx = {}
            for lt, ws_i in iidx.iteritems():
                new_ws_i = [wi for wi in ws_i if wi not in conflict]
                if new_ws_i:
                    new_iidx[lt] = new_ws_i

            search(new_iidx, layer + 1)


search(iidx, 0)
print(result)