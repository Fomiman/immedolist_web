from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Schedule(Base):
    __tablename__ = 'schedules'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    details = Column(Text, nullable=True)
    priority = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=True)
    
    def __repr__(self):
        return f"<Schedule(title='{self.title}', priority={self.priority}, due_date={self.due_date})>"

# SQLite 사용을 위한 엔진 설정
engine = create_engine('sqlite:///immedolist.db', echo=True)

# 모든 정의된 테이블 객체를 기반으로 데이터베이스 테이블 생성
Base.metadata.create_all(engine)

# 세션 생성을 위한 세션 팩토리 설정
Session = sessionmaker(bind=engine)
session = Session()

# 예시: 새로운 일정 추가
new_schedule = Schedule(title='Project Meeting', details='Discuss project milestones and updates', priority=2, due_date=datetime(2024, 5, 15))
session.add(new_schedule)
session.commit()

# 예시: 모든 일정 조회
all_schedules = session.query(Schedule).all()
for schedule in all_schedules:
    print(schedule)
