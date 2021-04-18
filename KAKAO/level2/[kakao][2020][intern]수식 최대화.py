# [kakao][2020][intern]수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

import re
from copy import deepcopy
from collections import deque
from itertools import permutations
def solution(expression):
    answer = 0
    nums = list(map(int, re.split('[+\-*]',expression)))
    ops = re.split('\d+',expression)[1:-1]
    expression = deque()
    for i in range(len(ops)):
        expression.append(nums[i])
        expression.append(ops[i])
    expression.append(nums[-1])

    for op_set in permutations(['+','-','*']):
        result = deepcopy(expression)
        for op in op_set:
            while op in result:
                num1 = result.popleft()
                oop = result.popleft()
                if oop != op:
                    result.append(num1)
                    result.append(oop)
                    continue
                num2 = result.popleft()
                if oop == '+':
                    result.append(num1 + num2)
                elif oop == '-':
                    result.append(num1 - num2)
                elif oop == '*':
                    result.append(num1 * num2)
        answer = max(answer, abs(*result))

    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))