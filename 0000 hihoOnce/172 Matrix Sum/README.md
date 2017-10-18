- 时间限制:10000ms
- 单点时限:1000ms
- 内存限制:256MB

## 描述

You are given an N × N matrix. At the beginning every element is 0. Write a program supporting 2 operations:

1. Add x y value: Add value to the element Axy. (Subscripts starts from 0
2. Sum x1 y1 x2 y2: Return the sum of every element Axy for x1 ≤ x ≤ x2, y1 ≤ y ≤ y2.

## 输入

The first line contains 2 integers N and M, the size of the matrix and the number of operations.

Each of the following M line contains an operation.

1 ≤ N ≤ 1000, 1 ≤ M ≤ 100000

For each Add operation: 0 ≤ x < N, 0 ≤ y < N, -1000000 ≤ value ≤ 1000000

For each Sum operation: 0 ≤ x1 ≤ x2 < N, 0 ≤ y1 ≤ y2 < N

## 输出

For each Sum operation output a non-negative number denoting the sum modulo 109+7.

### 样例输入
```
5 8
Add 0 0 1
Sum 0 0 1 1
Add 1 1 1
Sum 0 0 1 1
Add 2 2 1
Add 3 3 1
Add 4 4 -1
Sum 0 0 4 4
```

### 样例输出
```
1
2
3
```

# 《Matrix Sum》题目分析

这是一道非常经典的二维树状数组(Binary Indexed Tree)的题目。树状数组与线段树有着相同的很优秀的时间复杂度（一般是O(logN)完成某些修改、查询操作），同时更容易实现，并且往往复杂度的常数更小。

我们首先来看一下一维数状数组的问题。注意一下对于数状数组的讨论中，数组下标都是从1开始的。

假设我们有一个数组A[1..N]。一维树状数组可以支持对A[]进行如下操作：

1. add(index, val): 修改A[index]的值，累加val，也即A[index] += val
2. sum(index): 计算A[1] + A[2] + ... A[index]。

并且以上两种操作都能在O(logN)之内完成。注意我们能O(logN)求前缀和，意味着也可以O(logN)求区间和:A[i] + A[i+1] + ... + A[j]，只需要求sum(j) - sum(i-1)。而我们能对A[index]累加val，意味着实际上我们可以任意修改A[]每一个元素的值。

实际上，一维数状数组就是一个一维数组，我们不妨称之为BIT[1..N]，它的每一个元素与A[]有如下对应关系：

```
BIT[1] = A[1]
BIT[2] = A[2] + A[1]
BIT[3] = A[3]
BIT[4] = A[4] + A[3] + A[2] + A[1]
BIT[5] = A[5]
BIT[6] = A[6] + A[5]
BIT[7] = A[7]
BIT[8] = A[8] + A[7] + ... A[2] + A[1]
```

![tree array](https://media.hihocoder.com/contests/hiho172/week172-1.png)

形象一点讲就是：

```
0. 如果i是奇数，那么BIT[i] = A[i]
1. 如果i是2的倍数但不是4的倍数，那么BIT[i] = A[i] + A[i-1] (从A[i]开始2个数的和)
2. 如果i是4的倍数但不是8的倍数，那么BIT[i] = A[i] + A[i-1] + A[i-2] + A[i-3] (从A[i]开始4个数的和)
...
k. 如果i是2^k的倍数但不是2^(k+1)的倍数，那么BIT[i] 是 从A[i]开始2^k个数的和。
```

注意！划重点！对于一个整数x，BIT[x]的项数可以用一个非常简洁的函数求得，我们称之为lowbit，lowbit(x) = x & (-x)。其中&是与运算。用代码的表示就是：

```
int lowbit(int x) {
    return x & (-x);
}
```

假设我们已经有了BIT[]数组，我们就可以把sum(A[1..index])表示若干个(不超过log(index)个)BIT[]的元素之和:

```
sum(A[1..7]) = BIT[7] + BIT[6] + BIT[4]
sum(A[1..8]) = BIT[8]
sum(A[1..6]) = BIT[6] + BIT[4]
```

具体方法就是，我们要求sum(A[1..x])，我们先把BIT[x]加进去。我们知道BIT[x]是从A[x]开始的lowbit(x)个元素之和，也就是BIT[x] = A[x] + A[x-1] + ... + A[x - lowbit(x) + 1]，那么余下还没加的就是sum(A[1..(x - lowbit(x))]。于是我们再把BIT[x-lowbit(x)]加进去，…… 这样递归的把一个个BIT[i]加进去，直到这些BIT[i]完全覆盖了sum(A[1..x])。

代码如下：

```
int sum(int x) {
    int ret = 0;
    while(x > 0) {
        ret += BIT[x]);
        x -= lowbit(x);
    }
    return ret;
}
```

最后我们还剩下两个问题，对于给定的A[1..N]如何求出BIT[1..N]，以及当进行add(index, val)操作时，如何更新BIT[]数组。

我们不妨设一开始A[]数组每个元素都是0，(这时BIT自然也是全0)，对于指定的A[1..N]是经过N个add操作达成的，这样我们就只用解决一个问题：add操作。

当我们改变A[x]的值时，显然对于所有包含A[x]的BIT[i]都需要一起做出修改。例如修改了A[3]，那么BIT[3], BIT[4], BIT[8]都要一起修改。如果我们需要修改的BIT元素太多，或者求出哪些元素要修改的复杂度太高，都会影响到add操作的复杂度。

首先我们分析一下哪些BIT的值要修改。我们再回顾一下这个图：

![tree array](https://media.hihocoder.com/contests/hiho172/week172-1.png)

不难发现当我们修改A[x]时，恰好是BIT[x]以及BIT[x]的所有祖先都要修改。

注意！划重点！ BIT[x]的父节点是BIT[x + lowbit(x)]。所以add(x, val)用代码表示如下：

```
void add(x, val) {
    while(x <= N) {
        BIT[x] += val;
        x += lowbit(x);
    }
}
```

以上我们就搞定了一维树状数组，有没有发现代码都非常短 ：D

下面我将一维树状数组扩展到二维。

假设我们有二维数组A[1..N][1..N]，二维树状数组可以支持对A[][]进行如下操作：

```
1. add(x, y, val): A[x][y] += val
2. sum(x, y): 求和sum(A[1..x][1..y])
```

和一维情况类似，能支持以上两个操作实际就能支持任意修改A[x][y]的值以及求一个子矩阵A[a..b][c..d]的和。

二维树状数组以上两个操作的复杂度都是O((logN)^2)的。

二维树状数组BIT2[x][y]与A[][]的对应关系如下图：

![2D tree array](https://media.hihocoder.com/contests/hiho172/week172-2.png)

直观理解就是x坐标和y坐标分别是一个一维树状数组，假设一维情况中BIT[x]对应的是A[i1], A[i2] ... A[ik]， BIT[y]对应的是A[j1], A[j2], ... A[jt]。那么BIT2[x][y] 相当于笛卡尔积 {i1, i2, ... ik} x {j1, j2, ... jt}：

BIT2][x][y] = ΣA[i][j] | {i in {i1 ... ik}且 j in {j1 ... jt}}

于是add(x, y, val)可以用一个二重循环实现：

```
void add(int x, int y, int val) {
    for(int i = x; i <= N; i += lowbit(i)) {
        for(int j = y; j <= N; j += lowbit(j)) {
            BIT2[i][j] += val;
        }
    }
}
```

sum(x, y)求和也可以用一个二重循环实现：

```
int sum(int x, int y) {
    int ret = 0;
    for(int i = x; i > 0; i -= lowbit(i)) {
        for(int j = y; j > 0; j -= lowbit(j)) {
            ret += BIT2[i][j];
        }
    }
    return ret;
}
```