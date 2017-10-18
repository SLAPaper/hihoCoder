#include <iostream>
#include <vector>

const int BASE = 1e9 + 7;

using namespace std;

class treeMatrix
{
    typedef vector<int> vint;
    typedef vector<vint> vvint;

  public:
    const int N;
    vvint mat;

    treeMatrix(int N) : N(N), mat(vvint(N + 1, vint(N + 1)))
    {
    }

    ~treeMatrix()
    {
    }

    static int lowbit(int x)
    {
        return x & (-x);
    }

    static int mod(int a, int b)
    {
        if (b < 0)
        {
            return mod(a, -b);
        }
        int ret = a % b;
        if (ret < 0)
        {
            ret += b;
        }
        return ret;
    }

    void add(int x, int y, int val)
    {
        for (int i = x + 1; i <= N; i += lowbit(i))
        {
            for (int j = y + 1; j <= N; j += lowbit(j))
            {
                mat[i][j] = mod(mat[i][j] + val, BASE);
            }
        }
    }

    int _sum(int x, int y)
    {
        int ret = 0;
        for (int i = x + 1; i > 0; i -= lowbit(i))
        {
            for (int j = y + 1; j > 0; j -= lowbit(j))
            {
                ret = mod(ret + mat[i][j], BASE);
            }
        }
        return ret;
    }

    int sum(int x1, int y1, int x2, int y2)
    {
        return mod(_sum(x2, y2) - _sum(x1 - 1, y2) - _sum(x2, y1 - 1) + _sum(x1 - 1, y1 - 1), BASE);
    }
};

int main()
{
    int N, M;
    cin >> N >> M;

    treeMatrix tmat = treeMatrix(N);

    for (int i = 0; i < M; ++i)
    {
        string op;
        cin >> op;
        if (op == "Add")
        {
            int x, y, val;
            cin >> x >> y >> val;
            tmat.add(x, y, val);
        }
        else if (op == "Sum")
        {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            cout << tmat.sum(x1, y1, x2, y2) << endl;
        }
    }
    return 0;
}
