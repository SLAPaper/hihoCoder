- 时间限制:10000ms
- 单点时限:1000ms
- 内存限制:256MB

## 描述

Little Hi and Little Ho are playing a game. There is an integer array in front of them. They take turns (Little Ho goes first) to select a number from either the beginning or the end of the array. The number will be added to the selecter's score and then be removed from the array.

Given the array what is the maximum score Little Ho can get? Note that Little Hi is smart and he always uses the optimal strategy.

## 输入

The first line contains an integer N denoting the length of the array. (1 ≤ N ≤ 1000)

The second line contains N integers A1, A2, ... AN, denoting the array. (-1000 ≤ Ai ≤ 1000)

## 输出

Output the maximum score Little Ho can get.

### 样例输入

```
4
-1 0 100 2
```

### 样例输出

```
99
```

# 《A Game》题目分析
每次轮到小Hi或者小Ho时，他们都面临同样的二选一决策：是拿走最左边的数，还是拿走最右边的数？

当然可以暴搜。时间复杂度`O(2^N)`会超时。此外比较容易发现贪心策略——总是拿走更大的数——是错误的。样例就是范例。

其实本题是一道非常经典的动态规划题目。

由于每次只能从数组首/尾拿走一个数，所以小Hi和小Ho在任何时候面对的残局都只可能是一段连续的子数组`A[i..j]`。我们不妨用`f[i][j]`表示当面对`A[i..j]`，先手最多能获得的得分。

如果我们能计算出所有`f[i][j]`的值，那么显然`f[1][n]`就是最终答案。

其中`i = j`的情况`f[i][j]`的值是很容易计算的：`f[i][j]=A[i]`。因为只剩下`A[i]`一个数，先手只能拿走`A[i]`。

对于`i < j`的情况，先手P需要决策是拿走`A[i]`还是拿走`A[j]`?

如果拿走`A[i]`，那么对手Q面对的是`A[i+1 .. j]`，Q最多能获得的得分是`f[i+1][j]`。而且Q一定会按照得到`f[i+1][j]`这个得分的方式进行决策。所以先手P最大得分是`sum(A[i .. j]) - f[i+1][j]`。(`A[i .. j]`的分数和减去Q的得分)

同理如果拿走`A[j]`，先手P最大得分会是`sum(A[i .. j]) - f[i][j-1]`。

由于此时先手P可以二选一，所以

`f[i][j] = max{ sum(A[i .. j]) - f[i+1][j]`

`sum(A[i .. j]) - f[i][j-1] } = sum(A[i .. j]) - min(f[i+1][j], f[i][j-1])`

注意`sum(A[i .. j])`可以通过预处理出前缀和再O(1)计算得出。

# 经验

1. 注意 Python 数组的负索引，在 S 最后补一个零来把 i - 1 的条件判断简化掉
2. Windows 下的 python io 需要在读写切换的时候 flush 一下，不然会 IOError Errno 0（[参考StackOverflow](https://stackoverflow.com/questions/11176724/python-file-operations)）