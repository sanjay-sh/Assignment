# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:32:07 2020

@author: Satvik"""
#!/usr/bin/python3
# Fibonacci numbers module
def fib(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
#if __name__ == "__main__":
#    f=fib(100)
#    print(f)
    
        


