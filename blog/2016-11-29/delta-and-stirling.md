---
title: 差分序列与Stirling数
create: 2016.11.29
modified: 2016.11.29
tags: 差分
      Stirling数
      多项式插值
---

[TOC]
# 差分序列与Stirling数
刚看完《组合数学》的这一节，写一点笔记。

## 差分序列
### 定义
设一个序列：

$$
h(0), h(1), h(2), h(3), h(4), \dots
$$

的**一阶差分序列**为：

$$
\Delta h(0), \Delta h(1), \Delta h(2), \Delta h(3), \dots
$$

其中：

$$
\Delta h(n) = h(n + 1) - h(n)
$$

同样，将差分出来的序列再次进行差分，可以得到**二阶差分序列**。因此，我们定义**零阶差分序列**就是原序列，**$p$阶差分序列**为：

$$
\Delta^{(p)} h(n) = \Delta^{(p - 1)} h(n + 1) - \Delta^{(p - 1)} h(n) \;\;\;\; (p \gt 0)
$$

差分序列有一种求导的意味。

### 多项式的差分序列
多项式$h(n) = 2n^3 + 2n^2 - 4n + 233$的差分序列如下：

$$
233, 233, 249, 293, 377, 513, \dots \\
0, \;16, \;44, \;84, \;136, \dots \\
16, \;28, \;40, \;96, \dots \\
12, \;12, \;12, \dots \\
0, \;\;0, \dots \\
\dots
$$

我们发现$h(n)$是个$3$次多项式，而它的序列经过$4$次差分就变成了全是$0$的序列。

可以证明，一个$p$次多项式的序列**最多经过**$p + 1$次差分就会变为全$0$序列。

首先考虑$0$次多项式，它的序列值是一个常数，所以至多经过一次差分就可以变为$0$。

现在进行归纳假设：假设对于$p$次多项式的序列最多经过$p + 1$次差分就会得到全$0$序列，那么现在证明对于$p + 1$次多项式最多差分$p + 2$次就可以得到全$0$序列。

观察最高次数的项，在每一次差分中的变化：

$$
\begin{aligned}
\Delta^{(c)} h(n) & = \Delta^{(c-1)} h(n + 1) - \Delta^{(c-1)}h(n) \\
& = (n + 1)^{p} + \cdots - n^p - \cdots \\
& = \sum_{k = 0}^p {p \choose k} n^k + \cdots - n^p - \cdots
\end{aligned}
$$

由于${p \choose p} = 1$，所以最高次数的项在一次差分中被减去了，所以差分后的序列是一个至多$p$次的多项式的序列。因此，根据归纳假设，$p + 1$次的多项式最多进行$p + 2$次差分就可以对到全$0$序列。

### 差分的线性性
如果：

$$
h(n) = af(n) + bg(n)
$$

那么：

$$
\begin{aligned}
\Delta h(n) & = \Delta (af(n) + bg(n)) \\
& = a(f(n + 1) - f(n)) + b(g(n + 1) - g(n)) \\
& = a\Delta f(n) + b\Delta g(n)
\end{aligned}
$$

由此我们证明了差分是一个线性变换。这称为差分的线性性。

### 特殊差分表
在差分表中：

$$
233, 233, 249, 293, 377, 513, \dots \\
0, \;16, \;44, \;84, \;136, \dots \\
16, \;28, \;40, \;96, \dots \\
12, \;12, \;12, \dots \\
0, \;\;0, \dots \\
\dots
$$

称第一横行为**第$0$行**，表示原数列，如上面的$233, 233, 249, 293, 377, 513, \dots$。而左边的第一斜列为**第$0$条对角线**，如上面的$233,0,16,12,0,\dots$。显然知道了这两个中的任意一个就可以确定整个差分表。

考虑一下由下面的**对角线**构成的差分表会是怎样的数列构成的：

$$
0, 0, 0, 0, 1, 0, 0\dots
$$

首先，这个差分表后面全部变成了$0$，所以这肯定是一个$4$次多项式的差分表。同时我们可以确定这个多项式有$4$个零点，所以我们可以写出：

$$
f(n) = cn(n-1)(n-2)(n-3)
$$

其中$c$还是待确定的。

同时，我们注意到$f(4) =  1$，所以：

$$
c \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 1 \Longrightarrow c = \frac1{4!}
$$

换言之：

$$
f(n) = {n! \over 4!(n - 4)!} = {n \choose 4}
$$

是不是感觉很神奇？这一结论可以推广到任意位置的$1$的差分表。同时，利用差分表的线性性，我们可以得到更加神奇的东西：

> 如果$\Delta f(n)$的第$0$条对角线为$c_0, c_1, c_2, c_3, \dots, c_p, 0, 0, \dots$，那么：
> $$ f(n) = \sum_{k=0}^p c_k{n \choose k}$$

此时你也许会想问这东西有什么用？由于它是对于一个多项式的差分分析得到的结论，因此，我们对于一个多项式，如果知道了第$0$条对角线，那么我们可以直接计算这个多项式。

并且，根据Pascal公式，我们可以知道：

$$
\sum_{k=0}^p {n \choose k} = {n + 1 \choose p}
$$

所以：

$$
\sum_{k = 0}^n f(k) = \sum_{k = 0}^p c_k {n + 1 \choose k}
$$

所以，当我们拥有了这个结论之后，我们就可以以同样的代价来计算它的前缀和。

现在来考虑一个具体一点并且不是很复杂的问题，但是可能当场并不能解决它：

> 给你$T$次询问，每次给出$n$和$p$，要求你计算：
> $$ \sum_{a = 1}^n a^p \pmod{10^9 + 7}$$
>
> $1 \leqslant T \leqslant 5000$，$1 \leqslant p \leqslant 5000$，$1 \leqslant n \leqslant 10^{18}$。

如果采用直接计算$c_0, c_1, c_2, \dots$的话，总的复杂度为$\Theta(q^3 + Tq)$。这里出现的问题就是系数的预处理代价太高，因此我们需要寻找一种更快速的计算方法。

对此，我们设$f_p(n) = n^p$，同时设它的系数为：

$$
c(p, 0), c(p, 1), c(p, 2), \dots, c(p, p)
$$

那么答案就是：

$$
\sum_{k = 0}^p c(p, k){n + 1 \choose k}
$$

## 第二类Stirling数
### 定义
有第二类Stirling数就有第一类Stirling数，但是由于第二类Stirling数可以帮助我们解决之前的问题，所以先介绍它。

第二类Stirling数的用途是使用**下降幂**来表示数的幂。下降幂是这样的一种东西：

$$
x^{\underline{n}} = {x! \over (x - n)!}
$$

回到前面的问题，可以发现：

$$
\begin{aligned}
n^p & = \sum_{k = 0}^p c(p, k){n \choose k} \\
& = \sum_{k = 0}^p \frac{c(p, k)}{k!} n^{\underline{k}}
\end{aligned}
$$

所以设：

$$
S(p, k) = {c(p, k) \over k!}
$$

为第二类Stirling数。并且满足：

$$
n^p = \sum_{k = 0}^p S(p, k)n^{\underline{k}}
$$

同时注意一下它的边界值：

$$
S(n, n) = 1 \;\;\;\; \forall n \in N \\
S(n, 0) = 0 \;\;\;\; \forall n \in N_+
$$

不妨来考虑一下：

$$
\begin{aligned}
n^{p-1} & = \sum_{k = 0}^{p-1} S(p-1, k)n^{\underline{k}} \\
n^p = n \cdot n^{p-1} & = n\sum_{k = 0}^{p-1} S(p-1, k)n^{\underline{k}} \\
& = \sum_{k = 0}^{p-1} S(p-1, k) \cdot n \cdot n^{\underline{k}} \\
& = \sum_{k = 0}^{p-1} S(p-1, k) \cdot (n - k + k) \cdot n^{\underline{k}} \\
& = \sum_{k = 0}^{p-1} S(p-1, k) n^{\underline{k + 1}} + \sum_{k = 0}^{p-1} kS(p-1, k) n^{\underline{k}} \\
& = \sum_{k = 1}^{p} S(p-1, k - 1) n^{\underline{k}} + \sum_{k = 0}^{p-1} kS(p-1, k) n^{\underline{k}}
\end{aligned}
$$

通过比较同一项的系数，我们可以得知下面的递推式：

$$
S(p, k) = kS(p - 1, k) + S(p - 1, k - 1)
$$

### 解决之前的问题
在之前的问题中，我们知道：

$$
\begin{aligned}
\sum_{a = 1}^n a^p & = \sum_{k = 0}^p c(p, k){n + 1 \choose k} \\
& = \sum_{k = 0}^p S(p, k)(n + 1)^{\underline{k}}
\end{aligned}
$$

对于后面的式子，我们发现可以通过递推算出$(n + 1)^{\underline{0}}$至$(n + 1)^{\underline{p}}$的值，同时，我们有了之前的递推式，我们可以在$\Theta(p^2)$的时间内预处理出第二类Stirling数。所以这个问题我们可以以$\Theta(p^2 + Tp)$的时间复杂度解决这个问题。

其实，根据第二类Stirling数的递推公式，我们也可以类似的推出$c(p, k)$的递推公式：

$$
c(p, k) = k(c(p - 1, k - 1) + c(p - 1, k))
$$

读者可以自己试一试。

但是这还不是这个问题的最优解法。使用伯努利数和快速傅里叶变换，我们可以得到更好的复杂度。这里就没有介绍了。

另外，使用拉格朗日插值法也可以快速求解这个问题，具体的可以参见[这篇博客](../2017-3-18/lagrange-interpolation.html)。

### 组合意义
现在来考虑一下这个简单问题：

> 求$p$个人，放入$k$个相同的房子 (房子不可以为空) 的方案数。

不难我们可以想出一个递推：设$f(p, k)$为$p$个人放入$k$个相同的房子的方案数，那么它满足：

$$
f(p, k) = kf(p - 1, k) + f(p - 1, k - 1)
$$

对于其正确性，考虑两点：

1. 如果第$p$个人单独进入一个房间，那么方案数为$f(p - 1, k - 1)$。
2. 如果第$p$个人进入之前的房间，那么它可以挑选之前的$k$个房间的任意一间，即方案数为$kf(p - 1, k)$。

同时我们注意到：

$$
f(n, n) = 1
$$

并且：

$$
f(n, 0) = 0 \;\;\;\; \forall n \in N_+
$$

也就是$f$和第二类Stirling数满足一样的初始条件和递推公式，那么意味着$f(p, k)$和$S(p, k)$是一样的。所以这个问题的答案就是$S(p, k)$。这也正是第二类Stirling数的组合意义。

对于这个问题，我们可以从容斥原理的角度来获得另外一个不同的公式。设$A_1,\; A_2, \;A_3,\dots,A_k$为第$1$到第$k$个房间为空的方案集合，那么我们的答案就是：

$$
S(p, k) = \frac1{k!}\left|\overline{A}_1 \cup \overline{A}_2 \cup \cdots \cup \overline{A}_k\right|
$$

注意在之前的推导里面我们区分了这$k$个房间，而第二类Stirling数是没有区分的，所以要乘以$1/k!$。

考虑到如果有$t$个房间为空，那么对于每一个人而言，就只有$k - t$个选择，所以对于此的方案数的就是$(k - t)^p$。所以我们可以知道：

$$
S(p, k) = \frac1{k!}\sum_{t = 0}^k (-1)^t{k \choose t}(k - t)^p
$$

这也就是计算单个第二类Stirling数的公式。

## 第一类Stirling数
### 定义
现在来介绍第一类Stirling数。与第二类Stirling数类似，第一类Stirling数是使用数的幂来表示下降幂。

现在来观察一下规律：

$$
\begin{aligned}
& n^{\underline{0}} = 1 \\
& n^{\underline{1}} = n \\
& n^{\underline{2}} = n(n - 1) = n^2 - n \\
& n^{\underline{3}} = n(n - 1)(n - 2) = n^3 - 3n^2 + 2n \\
& n^{\underline{4}} = n(n - 1)(n - 2)(n - 3) = n^4 - 6n^3 + 11n^2 - 6n \\
& \dots
\end{aligned}
$$

可以发现，下降幂展开以后是一个系数正负号交替的多项式。与在第二类Stirling数中类似的，我们设$s(p, k)$为第一类Stirling数，并且满足：

$$
n^{\underline{p}} = \sum_{k = 0}^p (-1)^{p - k}s(p, k)n^k
$$

以及边界值：

$$
s(n, n) = 1 \;\;\;\; \forall n \in N \\
s(n, 0) = 0 \;\;\;\; \forall n \in N_+
$$

类似的，我们可以据此推出第二类Stirling数的递推公式：

$$
\begin{aligned}
n^{\underline{p - 1}} & = \sum_{k = 0}^{p-1} (-1)^{p - k - 1}s(p - 1, k)n^k \\
n^{\underline{p}} & = (n - p + 1)\sum_{k = 0}^{p-1} (-1)^{p - k - 1}s(p - 1, k)n^k \\
& = \sum_{k = 0}^{p-1} (-1)^{p - k - 1}s(p - 1, k)n^{k+1} + \sum_{k = 0}^{p-1} (-1)^{p - k}(p - 1)s(p - 1, k)n^k \\
& = \sum_{k = 1}^{p} (-1)^{p - k}s(p - 1, k - 1)n^{k} + \sum_{k = 0}^{p-1} (-1)^{p - k}(p - 1)s(p - 1, k)n^k
\end{aligned}
$$

通过比较同次项的系数可以得知：

$$
s(p, k) = (p - 1)s(p - 1, k) + s(p - 1, k - 1)
$$

### 组合意义
同样的，第一类Stirling数也具有其组合意义。通过考虑下面的问题就可以证明：

> 求$p$个人围成$k$个圈 (圈不能为空) 的方案数。
> 注意这里的圈中的人的顺序不同也会视为圈不同。

对于这个问题，我们证明其答案$f(p, k)$满足下面的递推关系：

$$
f(p, k) = (p - 1)f(p - 1, k) + f(p - 1, k - 1)
$$

**证明**：

1. 如果第$p$个人独自站成一个圈，那么共有$f(p - 1, k - 1)$种方案。
2. 如果第$p$个人与之前的人站在一起，那么他有$p - 1$种方案站在一个人的右边，所以共有$(p - 1)f(p - 1, k)$中方案。

不难验证这个问题的初始条件与第一类Stirling数一致，所以$f(p, k)$和$s(p, k)$就是一样的啦～
