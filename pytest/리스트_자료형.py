
odd = [1,3,5,7,9]

a=[]
b=[1,2,3]
c=['Life','is','too','short']
d=[1,2,'Life','is']
e=[3,4,['too','short']] # list in list

print(d[2],d[3],e[2][0],e[2][1])
print(e[2][1])

print(d[:1])
print(d[:3])
print(e[:3])

# 리스트 연산
# 문자열 연산이랑 비슷하게 더하면 합쳐지고 곱하면 반복한다.
print(d+b)
print(d*3)

#길이 구하기
print(len(e))

#리스트 값 수정하기
e[1]=7
print(e)

# del 값 삭제(리스트나 지정된 변수 내용도 삭제 가능)
del e[1]
print(e)

del e[:1]
print(e)

# append 값 추가
e.append([1,2,3,4])# 뒤에 추가, 중간엔 안되나? => insert로 가능
print(e)
#e.append(5,6,7,8) 에러남. 마지막 자리에 한개의 값 또는 리스트만 추가 가능한 듯하다.
# extend(5,6,7,8)로 가능하다 뒤에 나옴
e.append(5)
print(e)

# sort 정렬 알파벳, 숫자 모두 가능
del a
a=[1,3,6,2,4,5]
a.sort()
print(a)

# reverse 뒤집기
a.reverse()
print(a)

# index 위치 반환
print(a.index(2))

# insert 원하는 자리에 값(요소) 추가
e.insert(0,1)
print("e =",e)

# remove(x) 리스트 내 제일 앞에 있는 x 제거
e[2].remove(4) #리스트 안의 리스트는 항상 따로 지정해줘야 되나보다.
print(e)

# pop() 리스트 내 요소 끄집어내기
# 리스트의 맨 마지막의 요소를 돌려주고 그 요소는 삭제한다.
print(a.pop())
print(a)
# 위치 지정해서 끄집어내기 가능함
print(a.pop(2))
print(a)

# count() 문자열과 동일함
# extend() 리스트를 확장한다. 여러 값을 한번에 추가 가능하며 안에 리스트형식으로만 넣어야한다. ex)extend([1,2,3,4])

