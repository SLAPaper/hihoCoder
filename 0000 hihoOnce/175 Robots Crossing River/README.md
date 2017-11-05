- 时间限制:10000ms
- 单点时限:1000ms
- 内存限制:256MB

## 描述

Three kinds of robots want to move from Location A to Location B and then from Location B to Location C by boat.

The only one boat between A and B and only one between B and C. Moving from A to B (and vise versa) takes 2 hours with robots on the boat. Moving from B to C (and vice versa) takes 4 hours. Without robots on the boat the time can be reduced by half. The boat between A and B starts at time 0 moving from A to B. And the other boat starts 2 hours later moving from B to C.

You may assume that embarking and disembarking takes no time for robots.

There are some limits:

1. Each boat can take 20 robots at most.
2. On each boat if there are more than 15 robots, no single kind of robots can exceed 50% of the total amount of robots on that boat.
3. At most 35 robots are allowed to be stranded at B. If a robot goes on his journey to C as soon as he arrives at B he is not considered stranded at B.

Given the number of three kinds robots what is the minimum hours to take them from A to C?

## 输入

Three integers X, Y and Z denoting the number of the three kinds of robots. (0 ≤ X, Y and Z ≤ 1000)

## 输出

The minimum hours.

### 样例输入
```
40 4 4
```

### 样例输出
```
24
```
# 题目解析

这道题目来源是某北美startup的面试题，看上去比较复杂，可能是为了考察候选人分析问题的能力？

首先需要看出整个流程的瓶颈完全在B-C这一段，换句话说我们只需求出所有机器人从B到C的最少时间，再加上2小时就是答案。事实上这个时间恰好等于把所有机器人直接从B运到C最少需要的船次x6。

如果没有“一船超过15个机器人则每种机器人不能超过半数”的限制，我们只需要20/船运走即可，最少船次是ceil((X+Y+Z)/20)。

由于有上面的限制，我们需要仔细讨论一下XYZ的相对大小。不妨设X >= Y >= Z，同时我们称三种机器人也为X、Y、Z类。

1. 如果X <= Y + Z，那么我们仍然可以20/船运走，同时所有船都没有机器人超过半数。 这种情况最少船次仍然是是ceil((X+Y+Z)/20)。
2. 如果X > Y + Z，这时我们没办法使所有船都载20机器人。但是我们当然希望能尽量派出载20机器人的船。于是有如下贪心策略：
    1. 首先尽量10个X类和10个非X类组成一船，派出若干船直到非X类不足10个机器人。
    2. 余下若干(不足10个)非X类机器人，配合尽可能多X类机器人组成一船。这里需要讨论余下的非X类机器人有多少个，不妨设为K。如果K不足8个，那么最多配合15-K个X类机器人，组成一船15个机器人；否则可以配合K个X类机器人，组成一船2K个机器人。
    3. 最后只剩下若干X类机器人，这些机器人只能15/船派出。

# 感想

看似条件很复杂结果是个贪心问题。船的交接时间刚好对的上以至于B处不能有超过35个机器人在等待的条件根本没用上。
