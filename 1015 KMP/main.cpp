#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> getNext(string p)
{
    vector<int> next = vector<int>(p.length());
    next.push_back(-1);

    int i = 0;
    int j = -1;

    while (i < p.length() - 1)
    {
        if (j == -1 || p[i] == p[j])
        {
            ++i;
            ++j;
            next.push_back(j);
        }
        else
        {
            j = next[j];
        }
    }

    return next;
}

int kmp_count(string o, string p)
{
    int i = 0;
    int j = 0;
    int count = 0;

    vector<int> next = getNext(p);

    while (i < o.length())
    {
        if (j == -1 || o[i] == p[j])
        {
            ++i;
            ++j;
        }
        else
        {
            j = next[j];
        }

        if (j == p.length())
        {
            count += 1;
            j = next[j - 1] + 1;
        }
    }

    return count;
}

int main()
{
    int N;
    cin >> N;

    for (int i = 0; i < N; ++i)
    {
        string p, o;
        cin >> p >> o;
        cout << kmp_count(o, p) << endl;
    }

    return 0;
}
