# [Ch15] 30 가사 검색
# 시간 복잡도 : 

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  left_index = bisect_right(a, left_value)
  right_index = bisect_right(a, right_value)
  return right_index - left_index

arr = [[] for _ in range(7)]
reversed_arr = [[] for _ in range(7)]

def solution(words, queries):
  answer = []
  for word in words:
    arr[len(word)].append(word)
    reversed_arr[len(word)].append(word[::-1])  #단어를 뒤집어서 삽입
  
  for i in range(7):
    arr[i].sort()
    reversed_arr[i].sort()

  print(reversed_arr)
  for q in queries:
    if q[0] != '?':
      res = count_by_range(arr[len(q)], q.replace('?','a'), q.replace('?','z'))
    else:
      res = count_by_range(reversed_arr[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
    
    answer.append(res)
  return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = solution(words, queries)
print(result)