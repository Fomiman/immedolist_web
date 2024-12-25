print("문자열 관련 함수")
# 기본적으로 자바 함수랑 거의 비슷한데 
# 일부 함수명이 조금 다르다.

print("")
a="hobby"
# 갯수 세기
print(a.count('b')) # 2
# 문자열 위치 찾기
print(a.find('y'))
print(a.find('k')) # 없을땐 -1을 반환한다.
# 위치 찾기 2
print(a.index('y'))
#print(a.index('k')) 없으면 에러 발생하고 멈춤

# 문자열 삽입
a=",".join('abcd')
print(a)

# 대/소문자 바꾸기
print(a.upper())
print(a.lower())

# 공백 지우기
b='  hi!   '
print(b.lstrip()+'!')
print(b.rstrip()+'!')
print(b.strip()+'!')

# 문자열 바꾸기
a='Life is too short'
print(a.replace("Life","Your life"))

# 문자열 나누기
print(a.split())#공백 기준으로 문자 나누기
b='a:b:c:d'
print(b.split(':'))#공백 기준으로 문자 나누기
