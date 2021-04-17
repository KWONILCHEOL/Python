# [kakao][2018][blind]비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

import re
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = bin(arr1[i]|arr2[i])[2:].zfill(n)
        temp = re.sub('[1]','#',temp)
        temp = re.sub('[0]',' ',temp)
        answer.append(temp)

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = 	[30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))    #["#####","# # #", "### #", "# ##", "#####"]

n = 6
arr1 = 	[46, 33, 33 ,22, 31, 50]
arr2 = 		[27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))    #["######", "### #", "## ##", " #### ", " #####", "### # "]