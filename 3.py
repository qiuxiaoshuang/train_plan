# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math
for num in range(1,10000):
    if math.sqrt(num+100) ==int(math.sqrt(num+100)) and math.sqrt(num+100+168) ==int(math.sqrt(num+100)):
        print(num)