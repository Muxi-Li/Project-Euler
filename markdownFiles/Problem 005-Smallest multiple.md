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
    :type return:bool
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

后来我谷歌了一下，才发现也可以这么解：

1. 求能被1到20的正数整除的最小数，实际是求1到20的最小公倍数。
2. 因为1到10的数乘以2都在11到20的范围内，所以求1到20的最小公倍数实际求11到20的最小公倍数就可以了。
3. 求11到20的最小公倍数，可以先求11和12的最小公倍数，然后再求这个最小公倍数和13的最小公倍数，一次类推，直到求出1到19的最小公倍数和20的最小公倍数，那么最后的结果就是1到20的最小公倍数。

<img src="C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574568786069.png" alt="1574568786069" style="zoom:67%;" />

----

#### 求两个数的最小公倍数

上面已经指出，可以挨个求出两个数的最小公倍数，以下是一些常用的求解方法。

1. 直接法

两个数a，b，它们的最小公倍数肯定落在[a, a*b]的范围内，所以在这个范围内，一旦第一个满足能够同时被a，b整除的就是a，b的最小公倍数了。

```python
def gcd(a, b):
    while i in range(a,a*b+1):
        if i % a == 0 and i % b == 0:
            return i
    return a*b
```



2. 先求最大公约数

* 更相减损术

> 更相减损术是出自《九章算术》的一种求最大公约数的算法，它原本是为约分而设计的，但它适用于任何需要求最大公约数的场合。

![1574570257876](C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574570257876.png)

用程序实现：

```python
def gcd(a, b):
    """
    : type a: int
    : type b: int
    功能：求a，b的最大公因数
    """
    # 使a指向最大值
    f = lambda a,b: (a,b) if a>b else (b,a)
    a, b = f(a,b)
    while b != 0:
    	a, b = b,a-b
    return a
```



* 辗转相除法

> 欧几里德算法是用来求两个正整数最大公约数的算法。是由古希腊数学家欧几里德在其著作《The Elements》中最早描述了这种算法,所以被命名为欧几里德算法。 

<img src="C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574571193335.png" alt="1574571193335" style="zoom:67%;" />

使用程序实现：

```python
def gcd(a, b):
    """
    : type a: int
    : type b: int
    功能：求a，b的最大公因数
    """
    # 使a指向最大值
    f = lambda a,b: (a,b) if a>b else (b,a)
    a, b = f(a,b)
    while b != 0:
    	a, b = b, a % b
    return a
```



----

#### 改进后的解法

* 方法一：化为求挨个两个数的最小公倍数的方法。至于求两个数的最小公倍数可以用上面的任何一种，优劣自己比较。

```python
def gcd(a, b):
    """
    : type a: int
    : type b: int
    功能：求a，b的最大公因数，辗转相除法
    """
    while b != 0:
        a, b = b, a % b
        # 更相减损术
        # a, b = b,a-b
    return a


def lcd(a, b):
    """
    : type a: int
    : type b: int
    功能：求a，b的最小公倍数
    """
    return (a * b) / gcd(a, b)

def main():
    num_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    a = num_list[0]
    b = num_list[1]
    for i in range(2, 10):
        # 调用求最小公倍数的函数
        lcd_num = lcd(a, b)
        a, b = lcd_num, num_list[i]
    print(a)
if __name__ == "__main__":
    main()
```

答案是：` 232792560 `

* 方法二：后来我又白嫖到了另一种方法。

把11到20的每个数分解质因数，例如：11 = 1×11,12 = 2^2×3,13 = 1×13,14 = 2×7,15 = 3×5,16 = 2^4,17 = 1×17,18 = 2×3^2,19 = 1×19,20 = 2^2×5，这样的话，包含的质数有2,3,5,7,11,13,17,19，也就是11到20的最小公倍数分解成最小公倍数后肯定是它们。这样的话，要求出11到20的最小公倍数，只需找出每个质数出现的最大幂，然后把它们相乘即可。本题可以这样求：最小公倍数 = 2^4×3^2×5×7×11×13×17×19，最后答案是：` 232792560 `。

所以现在问题分解为：

1. 将11到20的每个数分解质因数。
2. 找出每个质因数出现的最大幂指数。
3. 所有质因数的最大次幂的乘积。

<img src="C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574651413712.png" alt="1574651413712" style="zoom:67%;" />

```python
import math
def getPrimeFactors(n):
    """
    :type n: int
    :type return:list
    功能：将n分解质因数
    """
    i = 2
    # 存放质因数的列表
    primeFactor = []
    # 存放幂指数的列表
    exponent = []
    while i <= n:
        # 计数变量
        count = 0
        # 是否整除标志
        divided = False
        while n % i == 0:
            divided = True
            count += 1
            n /= i
        if divided:             # 如果i是n的质因数，那么将i和幂指数count存入相应列表
            primeFactor.append(i)
            exponent.append(count)
        i += 1
    return primeFactor,exponent
def f(p,e, primeFactor, exponent):
    """
    :type p:list
    :type e:list
    :type primeFactor:list
    :type exponent:list
    :type return:list
    功能：将p中的元素存入primeFactor中，前提是primeFactor中没有该元素。如果primeFactor中存在该元素，判断幂指数是不是最大。
    """
    for i,j in zip(p,e):
        if i not in primeFactor:
            primeFactor.append(i)
            exponent.append(j)
        else:
            # 判断primeFactor中的幂指数是不是最大
            e = exponent[primeFactor.index(i)]
            exponent[primeFactor.index(i)] = j if j >= e else e
    return primeFactor,exponent
def cal(a,b):
    return math.pow(a,b)
def main():
    number = [x for x in range(11, 21)]
    # 存放最终质因数的列表
    primeFactor = []
    # 存放最终幂指数的列表
    exponent = []
    for i in number:
        # 分解质因数
        p, e = getPrimeFactors(i)
        # 如果p中的质因数已经在primeFactor中存在，则判断exponent中的幂指数是不是最大
        primeFactor, exponent = f(p,e, primeFactor, exponent)
	# 计算两个列表中对应位置的元素的幂运算
    list1 = map(cal,primeFactor,exponent)
    result = 1
    # 将所有的幂运算结果进行乘积运算
    for i in list1:
        result *= i
    print(result)
if __name__ == '__main__':
    main()
```

个人怎么感觉这种解法分析挺简单，写起来还略显复杂，可能自己太菜了。

#### 官方解析





