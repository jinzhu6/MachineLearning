#coding:utf-8
'''
Created on 2015年5月18日

@author: xuzhenlei
'''
from time import sleep

from jug import TaskGenerator


@TaskGenerator
def is_prime(n):
    sleep(1.)
    for j in range(2, n - 1):
        if (n % j) == 0:
            return False
    return True
primes100 = [is_prime(n) for n in range(2, 101)]

