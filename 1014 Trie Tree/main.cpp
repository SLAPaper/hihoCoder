#include <iostream>
#include <map>
#include <string>

using namespace std;

class TrieTreeNode
{
  public:
    map<char, TrieTreeNode *> children;
    int count;

    TrieTreeNode()
    {
        this->count = 0;
    }
};

class TrieTree
{
  public:
    TrieTreeNode *root;

    TrieTree()
    {
        this->root = new TrieTreeNode;
    }

    void insert(string word)
    {
        auto current= this->root;
        for (auto c : word)
        {
            auto finding = current->children.find(c);
            if (finding == current->children.end())
            {
                current->children[c] = new TrieTreeNode();
            }
            current = current->children[c];
            current->count += 1;
        }
    }

    int query(string word)
    {
        auto current = this->root;
        for (auto c : word)
        {
            auto finding = current->children.find(c);
            if (finding == current->children.end())
            {
                return 0;
            }
            current = current->children[c];
        }
        return current->count;
    }

};

int main()
{
    int m, n;
    string s;

    auto trie = TrieTree();

    cin >> m;
    for (int i = 0; i < m; ++i)
    {
        cin >> s;
        trie.insert(s);
    }

    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> s;
        cout << trie.query(s) << endl;
    }
}
