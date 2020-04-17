"""
    作者：Muxi-Li
    时间：2020-04-17
    题目：The sum of the squares of the first ten natural numbers is,
          1^2+2^2+3^2+......+10^2 = 385
          The square of the sum of the first ten natural numbers is,
          (1+2+3+......+10)^2 = 55^2 = 3025
          Hence the difference between the sum of the squares of the first ten natural 
          numbers and the square of the sum is
          3025 - 385 = 2640
          Find the difference between the sum of the squares of the first one hundred 
          natural numbers and the square of the sum.
    题目描述：前10个自然数平方和是385，前10个自然是和的平方是3025，他们的差是2640，现在计算出前100个自然数两者的差。
    思路：初步感觉，两者都有公式计算，所以，嘿嘿嘿。
"""
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