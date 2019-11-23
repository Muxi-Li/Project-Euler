## Problem 005-Smallest multiple

#### 题目描述

>2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
>
>What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

已知2520是能被1到10内的整数整除的最小正数，现在要寻找能被1到20的整数整除的最小正数。

---

#### 涉及的数学知识

这道题应该没涉及什么数学知识吧，如果后面发现再补充。

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

那么怎么求两个数的最小公倍数呢？可以用辗转相除法啊，小学就学了。

----

#### 补充的数学知识





----

#### 官方解析

