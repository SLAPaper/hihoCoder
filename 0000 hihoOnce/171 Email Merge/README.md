- 时间限制:10000ms
- 单点时限:1000ms
- 内存限制:256MB

## 描述

You are given a list of usernames and their email addresses in the following format:

```
alice 2 alice@hihocoder.com alice@gmail.com
bob 1 bob@qq.com
alicebest 2 alice@gmail.com alice@qq.com
alice2016 1 alice@qq.com
```

Your task is to merge the usernames if they share common email address:

```
alice alicebest alice2016
bob
```

## 输入

The first lines contain an integer N, denoting the number of usernames. (1 < N ≤ 10000)

The following N lines contain N usernames and their emails in the previous mentioned format.

Each username may have 10 emails at most.

## 输出

Output one merged group per line.

In each group output the usernames in the same order as the input.

Output the groups in the same order as their first usernames appear in the input.

### 样例输入

```
4 alice 2 alice@hihocoder.com alice@gmail.com
bob 1 bob@qq.com
alicebest 2 alice@gmail.com alice@qq.com
alice2016 1 alice@qq.com
```

### 样例输出

```
alice alicebest alice2016
bob
```