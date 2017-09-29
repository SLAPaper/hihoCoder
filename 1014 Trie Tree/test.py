# generate 900k word and 900k query to test the runtime

from main import TrieTree
import time
import random

vocal = list(range(26))

trie = TrieTree()

words = [[random.choice(vocal) for _ in range(random.randrange(1, 11))] for _ in range(100000)]
queries = [[random.choice(vocal) for _ in range(random.randrange(1, 11))] for _ in range(100000)]

begin = time.time()

for word in words:
    trie.insert(word)

insert_end = time.time()

for query in queries:
    trie.query(query)

end = time.time()

print("insert time used:", insert_end - begin, 's')
print("query time used:", end - insert_end, 's')
print("time used:", end - begin, 's')
