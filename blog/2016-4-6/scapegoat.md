---
title: 替罪羊树(Scapegoat Tree)
create: 2016.4.6
modified: 2016.4.6
tags: 算法
      数据结构
      替罪羊树
---
[TOC]
# 替罪羊树(Scapegoat Tree)
## 热身：线性时间建树
**问题** 给定有序排好的元素序列，现在要你在$ \Theta(n) $的时间内建立一棵平衡的二叉搜索树。

最朴素的做法就是将元素逐一插入，由于许多平衡树的插入是$O(\log n)$的，因此总时间复杂度为$O(n\log n)$的。  
考虑到元素已经是排好序的，我们可以在这里做点优化。  
众所周知，二叉搜索树是有序的，即它的中序遍历是有序的。那么在它的中序遍历中，假设一个节点所处的位置为$i$，那么$i-1$就是它的左子树的大小，$n-i$就是右子树的大小。  
现在我们希望建一棵平衡二叉树，所以左右子树的大小应当相近。最优的情况为**左右子树大小一致**，此时该节点在中序遍历的最中间。

于是我们得到了一个较好的算法，就是选取中间的元素作为根节点，将序列切为两部分，递归的建立左右子树即可。对于每个元素需要花费$\Theta(1)$的时间来建立，总共有$\Theta(n)$个节点。因此该算法的时间复杂度为$\Theta(n)$。

```python
def build(s):
    return build(s, 1, len(s))
    
def build(s, left, right):
    if right < left:
        return None
    
    mid = (left + right) / 2
    node = new Node()                      # 新建节点
    node.left = build(s, left, mid - 1)    # 递归建立左子树
    node.right = build(s, mid + 1, right)  # 递归建立右子树
    node.update()                          # 对该节点做必要的更新
    
    return node
```

## α权重平衡
上面的热身非常简单。下面要讲的替罪羊树其实也很简单。在介绍替罪羊树之前，我们先了解下它的一个基本理论：**α权重平衡(α-weight-balanced)**。下文所述的平衡均为α权重平衡。

我们认为一棵树$x$是平衡的当且仅当它**每一棵子树**满足下列条件：

$$
\begin{aligned}
\text{size}(x.\text{left}) &\le \alpha \cdot \text{size}(x) \\
\text{size}(x.\text{right}) &\le \alpha \cdot \text{size}(x)
\end{aligned}
$$

其中，$ \alpha \in [0.5, 1] $。

这个$\alpha$可能会令人非常疑惑。我们首先来思考一下两个极值：$1$和$0.5$。  
当$a = 1$时，无论什么二叉树都会被视为平衡的，因为左右子树的大小不会超过这棵树的大小。这正对应着普通的二叉搜索树。  
而当$ a = 0.5$时，这时的要求将非常严格，左右子树的大小都必须是这棵树的大小的一半，此时只有完全二叉树能满足平衡要求。AVL树就是尝试保持这种平衡。  
我们都知道，二叉搜索树极易退化，而AVL树又为了平衡导致常数相当大，并且代码又臭又长，几乎没有人写。  
作为AVL树的改进，红黑树并不追求完美的平衡。通过放宽一些严格的平衡限制，保证了$ \alpha = 0.666\dots $的平衡，同时降低了常数，有着优良的性能。现在绝大多数语言的标准库都有它的身影。然而，红黑树对于OI竞赛而言代码量太大，不适合现场发挥。  
较为常用的Treap和Splay树则对$ \alpha$没有强制的限定，它们利用随机化的思想来使树尽可能平衡，即它们会尽量使$\alpha$值降低。我粗略测定了Treap、非旋转式Treap和Splay的$\alpha$。结果如下：

| BST \ 测试    |    1    |    2    |    3    |    4    |    5    |    平均   |  
|---------------|:-------:|:-------:|:-------:|:-------:|:-------:|:---------:|  
| Splay（5个不同数据） | 0.758   | 0.588   | 0.582   | 0.612   | 0.759   | **0.659** |  
| Treap（同一个数据） | 0.766   | 0.578   | 0.601   | 0.587   | 0.781   | **0.662** |  
| 非旋转式Treap（同一个数据） | 0.914   | 0.860   | 0.613   | 0.678   | 0.803   | **0.773** |

以上的结果仅供参考。可见一般的BST都能够使$\alpha$维持在$0.6$到$0.7$之间。  

## 替罪羊树
替罪羊树是一种平衡二叉树，它有一个很大的特点，就是它可以人为设定一个$\alpha$值，并且它会在操作中来维护指定的平衡。个人感觉替罪羊树“又懒又暴力”，但经过实测，它的速度完全不亚于上面提及的BST。

### 暴力重构
替罪羊树之所以能维持平衡，就是因为它把不平衡的树都暴力重构成一棵**完全二叉树**！  
但是这样一来时间复杂度就会暴涨。因此替罪羊树应当设置一个合适的$\alpha$值，避免过多的重构，从而均摊时间复杂度。可以证明，只要$\alpha$设置合理，替罪羊树的所有操作都是$O(\log n)$的。

首先考虑如何重构。在之前线性时间建树的基础上，我们先将树的中序遍历给复制出来，然后就可以直接在这个基础上重建。

### 查询
替罪羊树的查询和二叉搜索树一模一样，毕竟查找不会导致树的不平衡，那么它也没有必要进行重构。

### 插入
替罪羊树的插入操作和二叉搜索树是差不多的，只是最后要检查回溯时的树链上有哪棵子树违反了平衡。然后直接将其重构即可。

在重构时你可能会考虑到一条树链上可能有多个子树违反了平衡。对此，你只需要将最大的那棵子树重构即可。但是这样在实际代码中会略显复杂。如果你想偷懒，就只在回溯时找到了第一棵不平衡的树重构也是可以的。因为在替罪羊树中，同时出现几个不平衡的子树的情况也不是很多。在实际测试中，偷懒的写法在上千万的数据量下性能差距小于1s。

### 删除
替罪羊树的删除操作很好的体现了Lazy思想。它在删除节点时，并不是真正的删除，而是将其标记。此后所有的操作都将其无视，重构就直接丢弃，除非有插入操作将其恢复。当然我们不能无止尽地进行标记。如果被标记的节点数超过了整棵树大小的一半，我们就直接**将整棵树重构**，同时清除删除的节点。

### 实现细节及其时间复杂度
#### 节点定义
除了存储键值外，我们还需要存储树的大小和删除标记。

```python
struct Node<KeyType, ValueType>:
    key:     KeyType    # 键
    value:   ValueType  # 值
    size:    int        # 树的大小
    deleted: bool       # 删除标记
    left:    Node       # 左子树
    right:   Node       # 右子树
    
    def update(self):
        self.size = self.left.size + self.right.size
        
        if not self.deleted:  # 如果自己不是被删除的节点
            self.size += 1

# 空结点
struct NoneNode<*, *>:
    key     = None
    value   = None
    size    = 0
    deleted = True
    left    = NodeNode()
    right   = NodeNode()
    
    def update(self):
        pass
```

#### 选定α
替罪羊树的好处在于我们有了更好的调控能力。$\alpha$这个值可以选取$0.5$到$1$中的任意一个值。一般情况下选取$0.7$到$0.8$最佳。我们可以根据实际需要来作出适当调整。$\alpha$越大插入速度就越快，而访问和删除速度就会降低。反之则插入变慢。这里我们选择$0.75$：

```python
ALPHA = 0.75
```

#### 重构
重构操作十分简单，只需要中序遍历一遍就可以重建树了。

```python
# 中序遍历
def travel(h, s):
    if h is NoneNode:
        return

    travel(h.left, s)
    if h is not deleted:  # 忽略删除的节点
        s.append(h)
    travel(h.right, s)

    if h is deleted:
        del h

def refact(h):
    assert h is not NoneNode

    s = []
    travel(h, s)

    # 重建
    return build(s)
```

#### 插入
插入操作与二叉搜索树一致，只是在最后要重新从顶向下检查一遍是否有不平衡的子树。如果有就重构。

```python
def check(h, key):
    if h is NoneNode:
        return NoneNode()
    elif max(h.left.size, h.right.size) > ALPHA * h.size:
        return refact(h)
    elif key < h.key:
        h.left = check(h.left, key)
    elif key > h.key:
        h.right = check(h.right, key)
    
    h.update()
    return h
```

#### 删除
当我们命中删除的节点时，直接将其作删除标记，然后退回。删除结束后，检查整棵树中被删除的节点数是否超过了总结点数的一半，如果超过就整体重构。

```python
# 命中时
h.deleted = True
h.update()
deleted_count += 1

# ...

# 删除完后
if deleted_count > size / 2:
    tree = refact(tree)
    size -= deleted_count
    deleted_count = 0
```

#### 时间复杂度
替罪羊树的所有操作均摊复杂度为$O(\log n)$。

| 操作 | 时间复杂度（均摊） |
|:----:|:------------------:|
| 查询 | $O(\log n)$        |
| 插入 | $O(\log n)$        |
| 删除 | $O(\log n)$        |

对于**查询**操作，因为替罪羊树是保持了$\alpha$平衡的.只要$\alpha$值是合理的，那么这棵树就能保持比较平衡的状态，故插入是$O(\log n)$的。

对于**插入**操作，我们假设一个刚好重构过的子树的大小为$x$。在最坏情况下，我们可以向它的一侧不停的插入节点。假设当向一侧插入了$k$个节点时恰好破坏了平衡，那么此时$k$将满足：
$$ \left\lfloor\frac{x}{2}\right\rfloor + k \gt \alpha \cdot (x + k) $$

即
$$ k > {\alpha - \frac{1}{2} \over 1 - \alpha}x $$

因此每${\alpha - \frac{1}{2} \over 1 - \alpha}x $次就会进行一次重构。重构的时间复杂度为$\Theta(x)$。我们均摊它的时间复杂度：
$$ {\Theta(x) \over (\alpha - \frac{1}{2}) / (1 - \alpha) \cdot x} = \Omega(1) \; (\alpha = 0.75) $$

因此最好情况下我们可以均摊到$\Omega(1)$。由于树能保持$\alpha$平衡，因此插入操作的时间复杂度为$O(\log n)$。  
同时我们可见，$\alpha$越大，均摊的常数就会越低。

对于**删除**操作，我们假设我们进行了$\frac{n}{2}$次删除，并且为此触发了重构。由于每次删除的时间复杂度为$O(\log n)$的，因此总的时间复杂度为：
$$ \sum_1^{\frac{n}{2}} O(\log n) + \Theta(n) = \frac{n}{2}O(\log n) + \Theta(n) $$

我们将其均摊到$\frac{n}{2}$次操作上：
$$ {\frac{n}{2}O(\log n) + \Theta(n) \over \frac{n}{2}} = O(\log n) + \Theta(1) = O(\log n) $$

最终的时间复杂度为$ O(\log n) $。

## 更多操作
替罪羊树作为一种“又懒又暴力”的平衡二叉树，代码简单易于实现，并且性能十分不错。当然我们会想拓展更多的操作。当然，由于替罪羊树只会定时重构，不依赖其它的操作，因此可以扩展许多操作。下面列举一些：

* `rank`取排名：记录了子树的大小就可$O(\log n)$求出了。  
* 第k大：记录了`size`可以$O(\log n)$求出。  
* `split`拆分：非旋转式Treap的搞法即可，$O(\log n)$。  
* `merge`合并按照可合并堆的搞法即可，$O(\log n)$。  
* `slice`提取区间Splay乱搞，$O(\log n)$。  
* 各种区间操作，乱套各种树...$O(\log n)$、$O(\log n)$、$O(\log n)$...  
* ...  
* （当然有些时候何苦来乱搞）
