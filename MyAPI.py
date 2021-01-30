import sys
input = sys.stdin.readline
sys.stdin.read().splitlines()  #여러줄 입력

from math import gcd
def lcm(a, b):
    return a * b / gcd(a,b)

x = ['a','b']
':'.join(x)     ->'a:b'
*x              ->'a:b'

x = [1,2]
':'.join(map(str,x))    ->1:2
*x                      ->1:2

for a,b in zip([1,2,3,4],[5,6,7,8]):
-> a,b = (1,5), (2,6), (3,7), (4,8)

def rotate_martix_90degree(a):
  n = len(a)
  m = len(a[0])
  right90 = [[0] * n for _ in range(m)]
  left90 = [[0] * n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      right90[j][n-i-1] = a[i][j]   
      left90[n-j-1][i] = a[i][j]
  return right90
 
from bisect import bisect_left, bisect_right
  right_index = bisect_right(arr, right_value)
  left_index = bisect_left(arr,left_value)

def quick_sort(arr):
    if not arr: return []
    pivot = arr[len(arr)//2]
    lesser, equal, greater = [], [pivot], []

    for pos in arr:
        if pos[0] < pivot[0]:
            lesser.append(pos)
        elif pos[0] > pivot[0]:
            greater.append(pos)
        elif pos[0] == pivot[0]:
            if pos[1] < pivot[1]:
                lesser.append(pos)
            elif pos[1] > pivot[1]:
                greater.append(pos)

    return quick_sort(lesser) + equal + quick_sort(greater)
    

import sys
from bisect import bisect_right as br
input = sys.stdin.readline
def main(f=None):
    init(f)
    #sys.setrecursionlimit(10**9)
    
    N = int(input())
    arr = [int(i) for i in input().split()]
    targetSum = int(input())
    
    wrapper = BisectWrapper(arr, targetSum)
    idx = br(wrapper, -1, 0, max(arr)+1) - 1
    print(idx)
def sumWithUpperbount(arr, x, targetSum):
    sum_ = 0
    for i in arr:
        if i < x:
            sum += i
        else:
            sum += x
    
    if sum_ <= targetSum:
        return True
    else:
        return False
class BisectWrapper:
    def __init__(s, arr, targetSum):
        s.arr = arr
        s.targetSum = targetSum
    def __getitem__(s,n):
        return sumWithUpperbound(s.arr, n, s.targetSum)
        

#다른 값 찾기
arr, ans = [1,2,3], [3,4,5]
ans = list(set(arr).difference((set(ans))))
