## 写在前面
最近开始用python在Project-Eluer网站上刷题，想把每道题的解法记录下来，也是一种自我的提升。

网站地址：[Project-Euler](https://projecteuler.net/)

ok，现在开始记录每一道题，总结每道题的各种解法。

[Problem 001-Multiples of 3 and 5](https://github.com/Muxi-Li/Project-Euler/blob/master/Problem001-Multiples%20of%203%20and%205)
## Problem 001-Multiples of 3 and 5
#### 问题描述

>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
>
>Find the sum of all the multiples of 3 or 5 below 1000.

什么意思呢？比如说，在10以内的**自然数**，能够整除3或者5的数是3，5，6，9，它们的和是3+5+6+9=23，现在题中要求的是在1000以内的能够整除3或者5的数它们的和！没错，就是这个意思。

#### 我的最初思考

既然这道题只是要求在1000以内，很多人都可以想到直接暴力求解，也就是从0到999，找到能够整除3或者5的数，然后把这些数累加即可，那下面就试一试。

#### 我的解法

```python
sum = 0
for i in range(1, 1000):
    # print(i)
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
```



在语法上再改进一点：

```python
num = [x for x in range(1000) if x%3==0 or x%5==0]
sum_num = sum(num)
print(sum_num)
```

答案是： `233168 `。

答案是正确的，本以为这样就可以结束了，但新的问题就出现了，如果题中要求的是在一百万内求满足条件的数的和呢？还要用这种在一百万内循环挨个判断的解法吗？

#### 官方解析

我们再回过去想想，某个数能够整除3或者5，也就说在一百万内找3或者5的倍数，然后把它们累加。

在10以内满足条件的数是：3，5，6，9，则和可以表示为：`sum`=3+5+6+9=3×(1+2+3)+5×1。

如果在20以内呢？

`sum`=3+5+6+9+10+12+15+18=3×(1+2+3+4+5+6)+5×(1+2+3)-15，15重复了，所以要减掉。

那如果在一百万以内呢？

`sum`=3+5+6+9+10+12+15+18+...+999995+999996+999999=3×(1+2+3+...+333333)+5×(1+2+3+...+199999)-15×(1+2+3+...+66666)。

到这里就非常明显了，把非常浪费时间和内存的循环问题化成纯粹的数值计算问题！甚至求一千万内满足条件的数的和也不是问题！

```python
def sum_value(n, M):
    """
    功能：求出在小于M的所有n的倍数和
    参数：
        n：数 3或者5或者15
        M：条件  一百万
    """
    # 如果能整除还要减掉1，比如10以内，那么就不能包括10
    if M % n == 0:
        max = int(M/n) - 1
	else:
        max = int(M/n)
    sum = n*(1 + max)*max/2
    return sum
def main():
    # 主函数
    # 1。计算在条件以内的3的倍数的和
    sum_3 = sum_value(3, 1000000)
    # 2.计算5的倍数的和
    sum_5 = sum_value(5, 1000000)
    # 3.计算15的倍数的和
    sum_15 = sum_value(15, 1000000)
    print(sum_3 + sum_5 - sum_15)
if __name__ == "__main__":
    main()
```

