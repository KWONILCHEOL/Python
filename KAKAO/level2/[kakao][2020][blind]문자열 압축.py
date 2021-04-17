# [kakao][2018][blind]다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(s):
    length = len(s)
    answer = length

    for step in range(1, length // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, length, step):
            if prev == s[j : j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer

# def compress(s, tok):
#     words = [s[i:i + tok] for i in range(0, len(s), tok)]
#     res = []
#     cur_word = words[0]
#     cur_cnt = 1
#     # words[1:] + ['']의 ['']는 리스트의 개수를 맞춰줌
#     for a, b in zip(words, words[1:] + ['']):
#         if a == b:
#             cur_cnt += 1
#         else:
#             res.append([cur_word, cur_cnt])
#             cur_word = b
#             cur_cnt = 1
#
#     return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
#
# def solution(s):
#     return min(compress(s, tok) for tok in list(range(1, int(len(s) / 2) + 1)) + [len(s)])

print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))