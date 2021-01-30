import heapq

def solution(food_times, k):
  if sum(food_times) <= k:
    return -1

  q = []
  length = len(food_times)
  for i in range(length):
    heapq.heappush(q, (food_times[i], i + 1))

  sum_value = 0
  previous = 0

  #sum_value + (현재의 음식 시간 - 이전 음식 시간) * (현재 음식 개수)를 k와 비교
  while sum_value + ((q[0][0] - previous) * length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous) * length
    length -= 1
    previous = now
  
  result = sorted(q, key = lambda x : x[1])
  return result[(k - sum_value) % length][1]

print(solution([3,1,2], 5))