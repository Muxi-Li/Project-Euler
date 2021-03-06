## Problem 002-Even Fibonacci numbers

#### 问题描述

>Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
>
>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

这道题是什么意思呢？

大家都知道斐波那契数列吧？斐波那契数列就是从1和2开始的数列，之后的每一项都等以它之前两项的和，比如数列的第三项为3，3=1+2，第四项为5，5=3+2.....

这道题要求的是在斐波那契数列中，最大数不超过**四百万**，并且求整个数列的**偶数**的**和**！！！！四百万啊！！！！



---

#### 我的思考

原谅我头脑简单，一开始的想法就是真的直接列出不超过4百万的数列，然后判断是不是偶数，满足偶数条件就累加和！我也却是这样做了。下面试一试着略显低下很暴力的解法！



----

#### 我的解法

```python
def isEven(n):
    # 判断偶数
    return n%2==0

def sumEvenFibo(n):
    """
    参数：
        n：最大数范围
    返回：偶数列的和
    """
    """
    1,2,3,5,8.....
    a,b,c
    """
    a = 1
    b = 2
    c = 0
    sum_fibo = 2
    # n = 4000000
    while c <= n:
        c = a + b
        a,b = b,c
        if isEven(c):
            sum_fibo += c
    return sum_fibo

def main():
    # 主函数
    sum_fibo = sumEvenFibo(4000000)
    print(sum_fibo)
if __name__ == "__main__":
    # 主进程
    main()
```

答案：` 4613732 `

还好是对的，不过这样解真的是入不了眼啊！！！！还是看官方解答吧，我没有思路。



----

#### 官方解析

##### 解法1

![1573191086165](‪../img/1.png)


我们在数列的第一项添加1，那么对整道题的求解不会造成影响，因为1不是偶数。从上面可以发现，偶数也就是红色部分都是每一组的第三个数！！这对我上面的求解会有什么促进改进的地方呢？既然已经知道每组的第三个数是偶数，那么我们就可以省略判断偶数的步骤了！这对于要判断4百万个数是不是偶数是有很大的进步的！

那么下面就是改进后的程序：

```python
def sumEvenFibo(n):
    """
    参数：
        n：最大数范围
    返回：偶数列的和
    """
    """
    1,1,2,3,5,8.....
    a,b,c,a,b,c.....
    """
    a = 1
    b = 1
    c = 2
    sum_fibo = 0
    while c <= n:
        sum_fibo += c
        a = b + c
        b = a + c
        c = a + b
    return sum_fibo


def main():
    # 主函数
    sum_fibo = sumEvenFibo(4000000)
    print(sum_fibo)

if __name__ == "__main__":
    # 主进程
    main()
```

##### 解法2

前面省略了判断偶数的步骤，还有没有更容易计算的方法呢？

现在单独把斐波那契数列中偶数拿出来，单独组成一个数列，如下：

2，8，34，144......

他们之间有没有什么关系呢？官方确实给出来一个公式，从公式中可以得出该数列的每一个数，公式如下：

 ` E(n)=4*E(n-1)+E(n-2) `，比如第三项为34，34=4×8+2

证明过程如下：

F(n) = F(n-1) + F(n-2) 

​		= F(n-2)+F(n-3)+F(n-2)=2 F(n-2) + F(n-3) 

​		= 2(F(n-3)+F(n-4))+F(n-3))

​		=3 F(n-3) + 2 F(n-4) 

​		= 3 F(n-3) + F(n-4) + F(n-5) + F(n-6) 

​		= 4 F(n-3) + F(n-6) 

这样的话，我们的问题就不是在斐波那契数列中求解了，而是从它的衍生数列中找到没有超过4百万的数的最大值，然后把它之前的数累加，这期间省掉了很多不是必要的数，也算是很大改进了吧（我真想不到这里）。

对应的程序如下：

```python
def sumEvenFibo(n):
    a = 2
    b = 8
    c = 4*b + a
    sum_fibo = a + b + c
    while True:
        a, b, c = b, c, 4*c+b
        if c>n:
            break
        sum_fibo += c
    return sum_fibo
def main():
    # 主函数
    sum_fibo = sumEvenFibo(4000000)
    print(sum_fibo)
if __name__ == "__main__":
    # 主进程
    main()
```

