'''
대응 관계를 나타내는 자료형
key : value를 한쌍으로 가지는 자료형이다.
리스트나 튜플처럼 순차적으로 요솟값을 구하지 않고 
key를 통해서 value를 얻어온다.
'''

# 딕셔너리 기본형태
#{key1:value1,key2:value2,key3:value3}

exdic={"name":"yongwon","k_age":32,"age":31} # value에는 리스트 타입도 올 수 있다.

# 딕셔너리 쌍 추가하기
exdic[3]='a' # key가 3, value가 a인 쌍 추가

print(exdic)

# 요소 삭제
del exdic[3] #key가 3인 쌍 삭제

# key통해서 value얻기
print(exdic["name"])




