- 时间限制:10000ms
- 单点时限:1000ms
- 内存限制:256MB

## 描述

What is possibility of rolling N dice and the sum of the numbers equals to M?

## 输入

Two integers N and M. (1 ≤ N ≤ 100, 1 ≤ M ≤ 600)

## 输出

Output the possibility in percentage with 2 decimal places.

### 样例输入
```
2 10
```
### 样例输出
```
8.33
```

# 讨论

比较容易的动态规划。

用f[i][j]表示掷了i枚骰子，点数之和是j的概率。

递推方程留给大家推导~

提示：考虑最后一枚骰子的点数

# 感想

和斐波那契数列一个思路，每一项只依赖前六项，无脑记忆化递归即可压线通过，空间复杂度 O(nm)。

想要节约空间的话可以改成递推式，保存 n-1 的所有状态即可计算 n 的所有状态，空间复杂度是 O(m)。
