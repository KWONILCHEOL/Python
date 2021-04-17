# [kakao][2021][blind]신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

from re import sub
def solution(new_id):
    st = new_id
    st = st.lower()
    st = sub('[^a-z0-9\-_.]','',st)
    st = sub('\.+','.',st)
    st = sub('(^\.)|(\.$)','',st)
    st = 'a' if len(st) == 0 else st[:15]
    st = sub('\.$','',st)
    st = st if len(st) > 2 else st + ''.join(st[-1] for i in range(3-len(st)))
    return st

print(solution("...!@BaT#*..y.abcdefghijklm"))  #"bat.y.abcdefghi"
print(solution("z-+.^."))                       #"z--"
print(solution("=.="))                          #"aaa"
print(solution("123_.def"))                     #"123_.def"
print(solution("abcdefghijklmn.p"))             #"abcdefghijklmn"