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

* 怎么判断一个数是不是回文数？

我的做法是先将数值转换成字符串类型，然后将字符串转换成列表，将列表倒序输出，用新的的变量接收这个倒序的列表，然后看它们是否相等，如果相等，说明是这个数是回文数，如果不相等，说明不是回文数。

```python
def isPalindrome (n):
    """
    功能：判断是否是回文数
    """
    str_num = str(n)
    list_num = list(str_num)
    rev_list_num = list_num[::-1]
    # rev_list_num = list_num[x in list_num ]
    if list_num == rev_list_num:
        return True
    else:
        return False
```

* 怎么得到回文数？

一开始我是设置两个变量`m`，`n`，初始值都是100，然后设置变量`num`接收它们的乘积，首先`m`不变，`n`递增1，直到`n`到1000为止，如果`n`等于1000，那么`m`增1，这样下去循环直到`m`也到1000，整个循环结束，这样就得到了三位数乘积的所有回文数。

* 完整代码

```python
def isPalindrome (n):
    """
    功能：判断是否是回文数
    """
    str_num = str(n)
    list_num = list(str_num)
    rev_list_num = list_num[::-1]
    if list_num == rev_list_num:
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



