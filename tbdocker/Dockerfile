# 기본 베이스 이미지 사용
FROM rockylinux:9

# 필요한 패키지와 의존성 설치
RUN yum update -y && \
    yum install -y wget tar

# 사용할 포트 개방
EXPOSE 8629

# 호스트명 설정
ENV HOSTNAME=tbsvr

