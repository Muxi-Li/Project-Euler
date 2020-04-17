## Problem 006-Sum of squares and square of sum

### 题目

> The sum of the squares of the first ten natural numbers is,
>
> ​     1^2+2^2+3^2+......+10^2 = 385
>
> ​     The square of the sum of the first ten natural numbers is,
>
> ​     (1+2+3+......+10)^2 = 55^2 = 3025
>
> ​     Hence the difference between the sum of the squares of the first ten natural 
>
> ​     numbers and the square of the sum is
>
> ​     3025 - 385 = 2640
>
> ​     Find the difference between the sum of the squares of the first one hundred 
>
> ​     natural numbers and the square of the sum.

题目需要我们求出前100个自然数平方和与和的平方，他们之间的差值。

### 分析

这道题好像没有什么可以分析的，因为平方和与和的平方都是有公式的，直接可以求。或者用暴力求解吧，嘿嘿嘿。

**最终答案**：*25164150*

### 求解过程

#### 暴力求解

```python
sum_squares = 0
sum = 0
for i in range(1,101):
    sum += i
    sum_squares += i**2
print(sum**2-sum_squares)
```

直接遍历1到100的自然数，然后一边累加每个数，一边累加每个数的平方，最后将1到100的和平方，与另一个累加值求差值即可。

#### 公式求解

```python
def sum_squares(n):
    """
    :type n: int
    :return: int
    计算前n个自然数平方和
    """
    return n*(n+1)*(2*n+1)/6

def square_sum(n):
    """
    :type n: int
    :return:int
    计算前n个自然数的和的平方
    """
    return ((1+n)*n/2)**2


def main():
    a = sum_squares(100)
    b = square_sum(100)
    print(b-a)
if __name__ == "__main__":
    main()
```

等差数列的公式应该都懂，平方和公式百度都有，证明过程也有，详见[平方和公式](https://baike.baidu.com/item/平方和公式)



