# -*- coding: utf-8 -*-
'''
Created on Mon Mar  5 17:39:45 2018

'''
'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
因为153=1的三次方＋5的三次方＋3的三次方
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位
'''
l = []
for n in range(100,1000):
    i = n // 100 #i是n的百位数或者百位以上的数
    #注意Python3.x 取整为 //，而不是 /
    j = n //10 % 10 #j是n的十位数
    k = n % 10#k是n的个位数
    if n == i**3 + j**3 + k**3:
        if n == pow(i,3) + pow(j,3) + pow(k,3):
            l.append(n)
print(l)
print(len(l))
 
    