## Problem 005-Smallest multiple

#### 题目描述

>2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
>
>What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

已知2520是能被1到10内的整数整除的最小正数，现在要寻找能被1到20的整数整除的最小正数。

---

#### 我的思考

感觉如果单纯是解题而去的，完全可以用暴力求解。因为2520是能够被1到10整除的最小正数，所以可以设一个变量从2520开始，寻找能够被从11到20整除的最小正数，因为如果一个数能被11到20整除，那肯定能被1到10整除。

----

#### 我的解法

```python
def isDivided(m):
    """
    :type m: number
    : type return:bool
    判断m能不能被11到20的正数整除
    """
    dividedNmubers = [x for x in range(11,21)]
    f = lambda x,y: True if x % y == 0 else False
    for i in dividedNmubers:
        if not f(m,i):
            return False
    return True
def main():
    m = 2520
    while True:
        if isDivided(m):
            break
        m += 1
    print(m)
if __name__ == "__main__":
    main()
```

然而我错了，这个程序耗时非常的久，还没等结束我就按停了，根本没法用。

后来我去谷歌了下，了解到大概的解题思路。

整道题可以认为是在求1到20的最小公倍数，而11到20的最小公倍数肯定也是1到10的公倍数，所以问题变为求11到20的最小倍数。求那么多数的最小公倍数，可以化为先求前面两个数的最小公倍数，比如11和12，然后再求这个公倍数和13的最小公倍数，以此类推。。。。。

那么怎么求两个数的最小公倍数呢？

在数学上，两个数的最小公倍数等于两个数的乘积除以它们的最大公约数。

那又怎么求两个数的最大公约数呢？

可以用更相减损法或者辗转相除法。

所以整道题的解题思路可以改为：

<img src="C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574568786069.png" alt="1574568786069" style="zoom:67%;" />

----

#### 涉及的数学知识

* 更相减损术

> 更相减损术是出自《[九章算术](https://baike.baidu.com/item/九章算术/348232)》的一种求[最大公约数](https://baike.baidu.com/item/最大公约数/869308)的算法，它原本是为[约分](https://baike.baidu.com/item/约分/10107157)而设计的，但它[适用](https://baike.baidu.com/item/适用)于任何需要求最大公约数的场合。

![1574570257876](C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574570257876.png)

* 辗转相除法

> 欧几里德算法是用来求两个正整数最大公约数的算法。是由古希腊数学家欧几里德在其著作《The Elements》中最早描述了这种算法,所以被命名为欧几里德算法。 

<img src="C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574571193335.png" alt="1574571193335" style="zoom:67%;" />

----

#### 改进后的解法





#### 官方解析





