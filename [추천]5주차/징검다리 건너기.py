# [Ch15] 30 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060
# 시간 복잡도 : O(nlogm) m = 2e8
def solution(stones, k):
  answer = 0
  left, right = 0, int(2e8)

  while left <= right:  #O(logm)
    mid = (left + right) // 2
    s = list(stones)

    for i in range(len(s)):
      s[i] -= mid

    seq_minus, max_minus = 0, 0
    for i in range(len(s)):
      if s[i] < 0:
        seq_minus += 1
        if max_minus < seq_minus:
          max_minus = seq_minus
          if max_minus >= k:
            break
      else:
        seq_minus = 0

    if max_minus < k:
      if answer < mid:
        answer = mid
      left = mid + 1
    else:
      right = mid - 1
  return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))