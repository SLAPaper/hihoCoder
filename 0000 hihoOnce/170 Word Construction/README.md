- 时间限制:10000ms
- 单点时限:1000ms
- 内存限制:256MB

## 描述

Given N words from the **top 100 common words** in English (see below for reference), select as many words as possible **as long as no two words share common letters**.

Assume that the top 100 common words in English are:

the be to of and a in that have i it for not on with he as you do at this but his by from they we say her she or an will my one all would there their what so up out if about who get which go me when make can like time no just him know take people into year your good some could them see other than then now look only come its over think also back after use two how our work first well even new want because any these give day most us

## 输入

The first line contains an integer N, denoting the number of words. (1 ≤ N ≤ 40)

The second line contains N words from the top 100 common words.

## 输出

Output the most number of words can be selected.

### 样例输入

```
8
the be to of and a in that
```

### 样例输出

```
4
```

Tips： 'aeiou' 非常严格的限制了可行集，导致暴力搜索深度不超过5层，也就是极限 40 ** 5 = 102400000 这个级别的复杂度，这当然不能直接暴力，但是通过适当的剪枝可以达到目的
