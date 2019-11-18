## Problem 004-Largest palindrome product

#### 题目描述

>A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
>
>Find the largest palindrome made from the product of two 3-digit numbers.

最大的两位数乘积组成的回文数是9009，9009=91×99，现在寻找最大的由三位数乘积组成的回文数。



---

#### 涉及的数学知识

什么是回文数？

简单来讲，回文数就是正着读和反着读都一样的数字，比如 1234321 。

----

#### 我的思考

设置两个数`m`,`n`，初始值为999，然后设置循环，遍历999到100之间的数，得到它们的乘积，接着判断乘积是不是回文数，如果出现第一个回文数，那肯定是三位数乘积中最大的回文数。

关于怎么判断一个数是不是回文数，我想可以把数字转换成字符串，然后将字符串倒序，接着判断两个字符串相不相等。



----

#### 我的解法

* 怎么才能在三位乘积中循环不漏掉一个回文数呢？

<img src="C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574066189962.png" alt="1574066189962" style="zoom: 67%;" />

也就是对于每一个m值，都要从m到999循环一遍。

* 怎么判断一个数是不是回文数呢？

这里介绍两种简单方法。

1. 利用双指针

首先将两个三位数的乘积转换成字符串类型，然后设置两个类似c语言的指针，指向头尾，同时向中间移动，如果两个指针指向同一个元素之前都相等，那么这个数就是回文数。

<img src="C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574066612819.png" alt="1574066612819" style="zoom:50%;" />

```python
def isPalindrome (n):
    """
    功能：判断是否是回文数
    """
    str_num = str(n)
	i = 0
    j = len(str_num) - 1
    while i < j:
        if str_num[i] == str_num[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
```

2. 利用字符串切片

在将数值转换成字符串的基础上，可以利用字符串的切片操作倒序生成一个新的字符串，如果两个字符串相等，那么这个数就是回文数。

```python
def isPalindrome (n):
    """
    功能：判断是否是回文数
    """
    str_num = str(n)
    rev_num = str_num[::-1]
    if str_num == rev_num:
        return True
    return False
```

* 完整代码如下：

```python
def isPalindrome (n):
    """
    :type n:int
    功能：判断是否是回文数
    """
    str_num = str(n)
    rev_num = str_num[::-1]
    if str_num == rev_num:
        return True
    return False
def getMaxPalindrome():
    """
    返回：返回三位乘积中最大的回文数
    """
    m = n = 100
    # 存放回文数的列表
    list_pal = []
    while m < 1000:
        num = m * n
        # 调用判断回文函数
        if isPalindrome(num):
            list_pal.append([m,n,num])
        if n < 1000 and n != 999:
            n += 1
        else:
            m += 1
            n = m
            
    # 按list_pal每个元素列表中的第三个元素降序排列，第一个列表元素就包含最大回文数[913, 993, 906609]
    list1 = sorted(list_pal,key=lambda x: x[2],reverse=True)
    return list1[0]

def main():
    # 主函数
    # 1.调用回文函数
    max_pal = getMaxPalindrome()
    print("最大回文数：{}".format(max_pal))
if __name__ == '__main__':
    # 主进程
    main()
```

返回结果：

```python
[913, 993, 906609]
```

---

#### 官方解析

前面的程序是遍历所有的三位数的乘积，从中找到最大的回文数，能不能改进使遍历的数目减少呢？

上面是从100开始的，那么从999开始查找是不是更快的找到最大的回文数呢？

<img src="C:\Users\蔡\AppData\Roaming\Typora\typora-user-images\1574073691253.png" alt="1574073691253" style="zoom:67%;" />

我们以中间m = 566为例进行分析，n在每个循环中都是从999开始的，保证每次都能找到每个m对应的最大回文数，一旦在某个m的循环中发现回文数，即可跳出循环，进行下一个m的循环。

```python
def isPalindrome (n):
    """
    功能：判断是否是回文数
    """
    str_num = str(n)
    rev_num = str_num[::-1]
    if str_num == rev_num:
        return True
    return False
def getMaxPalindrome():
    """
    返回：返回三位乘积中最大的回文数
    """
    m = 999
    maxPal = 0
    while m >= 100:
        n = 999
        while n >= m:
            if m*n < maxPal:
                break
            if isPalindrome(m*n):
                maxPal = m * n
            n -= 1
        m -= 1
    return maxPal

def main():
    # 主函数
    # 1.调用回文函数
    max_pal = getMaxPalindrome()
    print("最大回文数：{}".format(max_pal))
if __name__ == '__main__':
    # 主进程
    main()
```

