#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> getNext(string p)
{
    vector<int> next = vector<int>(p.length());
    next[0] = -1;

    int i = 0;
    int j = -1;
    int m = p.length();

    while (i < m - 1)
    {
        if (j == -1 || p[i] == p[j])
        {
            next[++i] = ++j;
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
    int n = o.length();
    int m = p.length();

    int i = 0;
    int j = 0;
    int count = 0;

    vector<int> next = getNext(p);

    while (i < n)
    {
        if (o[i] == p[j])
        {
            if (j == m - 1)
            {
                count += 1;
                j = next[j];
            }
            else
            {
                ++i;
                ++j;
            }
        }
        else
        {
            j = next[j];
        }

        if (j == -1)
        {
            ++i;
            j = 0;
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
