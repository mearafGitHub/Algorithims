import heapq
from collections import Counter

fn = {}
fn[1] = 1
# def factorial(n):
#     if n == 0:
#         return 0
#     else:
#         r = _fct(n)
#         return r

def _fct(n):
    if n > 1:
        n *= _fct(n-1)
    return n

