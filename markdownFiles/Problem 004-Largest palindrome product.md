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

```python
def pal_jud(num):
    """
    功能：判断是否是回文数
    """
    str_num = str(num)
    list_num = list(str_num)
    rev_list_num = list_num[::-1]
    # rev_list_num = list_num[x in list_num ]
    if list_num == rev_list_num:
        return True
    else:
        return False
def pal():
    """
    功能：返回最大的回文数
    """
    m = n = 100
    list_pal = []
    while m < 1000:
        num = m * n
        # 调用判断回文函数
        if pal_jud(num):
            list_pal.append(num)
            # print(num)
        if n < 1000:
            n += 1
        else:
            m += 1
            n = m
    return max(list_pal)

def main():
    # 主函数
    # 1.调用回文函数
    max_pal = pal()
    print("最大回文数：{}".format(max_pal))
if __name__ == '__main__':
    # 主进程
    main()
```







---

#### 官方解析



