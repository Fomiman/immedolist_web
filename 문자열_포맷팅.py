
'''문자열 포맷팅'''
a="I eat %d apples." % 3
print(a)
#a="I eat %d apples." % "five" 에러남
'''
fiv="five"
a="I eat %s apples." % fiv => 이것도 가능
'''
a="I eat %s apples." % 'five'
print(a)
print()

'''
문자열 코드
%s : 문자열. (숫자형 중 정수 실수도 다 문자열로 바꿔서 바로 넣어준다.)
%c : 문자 1개
%d : 정수
%f : 부동 소수
%o : 8진수
%x : 16진수
%% : 문자 '%' 자체
'''

'''
정렬과 공백
'''
print("%10s" % "hi") # 전체 길이 10에 좌측 공백 8개 우측에 hi가 정렬되어서 나온다.
print("%-10sjane" % "hi") #좌측 정렬 후 10칸 채우고 다음 문자열 출력

# 소숫점 표현하기
print("%0.4f" % 3.1415926535)#소숫점 4자리까지만 표현
print("%10.4f" % 3.1415926535)#10자리 정렬+소숫점 4자리
print("%10.6f" % 3.1415926535)#10자리 정렬+소숫점 6자리


'''format 함수를 사용한 포맷팅'''
print("i eat {0} apples".format(3))

# 2개 이상의 값 
print("i eat {0} apples and {1} peaches.".format(3,1))
print("i eat {apl} apples and {pch} peaches.".format(apl=3,pch=1))

print("i eat {0} apples and {pch} peaches.".format(3,pch=1))
print("i eat {apl} apples and {0} peaches.".format(1,apl=3))
#이름과 인덱스 혼용 시 인덱스는 format 함수 내에서 순서를 지켜야 한다.
#print("i eat {apl} apples and {1} peaches.".format(apl=3,1)) => 인덱스 0을 대체해주지는 않는다.

#치환 + 정렬
# :< 좌측 정렬, :> 우측 정렬 꺽인 방향으로 정렬이다.
print("{0:<10}".format("Hi!"))
print("{0:>10}".format("Hi!"))
# :^ 가운데 정렬 - 가운데 정렬하면 좌측이 우선되는 듯
print("{0:^10}".format("Hi!"))

# 공백 채우기
print("{0:=^10}".format("Hi!"))
print("{0:!^10}".format("Hi!"))

# 소숫점
y= 3.1415926535
print("{0:0.4f}".format(y))

# { } 문자를 표현하고 싶을때는 2개 연속으로 사용하면된다.


# 문자열 포맷팅 파이선 3.6버전 부터는 f문자열 포맷팅이 가능하다.
name = '홍길동'
age = 30
t=f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(t)

t=f'저는 내년에 {age+1}살 입니다.'
print(t)

