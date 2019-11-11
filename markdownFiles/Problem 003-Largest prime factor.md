## Problem 003-Largest prime factor

#### 问题描述

>The prime factors of 13195 are 5, 7, 13 and 29.
>
>What is the largest prime factor of the number 600851475143 ?

prime factors也就是质因数，比如13195的质因数是5，7，13和29，现在要求出600851475143 最大的质因数。

----

#### 涉及的数学知识

* 因数：能够被某个数整除的数，比如18能够整除1，3，6，9，18，即它们都是18的因数。
* 质数： 质数又称素数，一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数。 比如数字3，除了1和3找不到一个能被它整除的数，所以它是质数。

* 质因数：**质因数**（**素因数**或**质因子**）在数论里是指能整除给定正整数的质数。

  比如18这个数，18=2×3×3，那么2和3就是18的质因数。

##### 质因数和因数的区别

质因数的重点是某个数的**因数**，还必须是**质数**。本道题就是求一个数的质因数，只不过数字很大。

---

#### 我的思考

假设题目中的数字为`n`。

既然要求最大的质因数，那么总该找出所有的质因数，然后比较才能得出最大的。



---

#### 我的解法

```python
import math
def getMaxPrimeFac(n):
    """
    参数：
        n：目标数字
    返回：该数字的最大质因数
    """
    # 存放质因数的列表
    list_fac = []
    a = 2
    while a <= n:
        if n % a == 0:
            list_fac.append(a)
            print(a)
            n /= a
        else:
            a += 1
    return max(list_fac)
def main():
    # 主函数
    n = 600851475143
    max_pri_fac = getMaxPrimeFac(n)
    print(max_pri_fac)
if __name__ == "__main__":
    # 主进程
    main()

```

#### 官方解法

```python
# Python3 code to find largest prime 
# factor of number 
import math 
  
# A function to find largest prime factor 
def maxPrimeFactors (n): 
      
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1
      
    # Print the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2 
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 
  
# Driver code to test above function 
n = 15
print(maxPrimeFactors(n)) 
  
n = 25698751364526
print(maxPrimeFactors(n)) 
  
# This code is contributed by "Sharad_Bhardwaj". 
```

代码地址：[GeeksforGeeks]( https://www.geeksforgeeks.org/python-program-for-find-largest-prime-factor-of-a-number/ )

