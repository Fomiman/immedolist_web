from models import Session, Schedule
from datetime import datetime

def add_schedule(title, details, priority, due_date):
    session = Session()
    new_schedule = Schedule(
        title=title,
        details=details,
        priority=priority,
        due_date=datetime.strptime(due_date, "%Y-%m-%d")
    )
    session.add(new_schedule)
    session.commit()
    print(f"Added new schedule: {title}")
    session.close()

def list_schedules():
    session = Session()
    schedules = session.query(Schedule).all()
    session.close()
    return schedules

# 예시: 컨트롤러 함수 테스트
if __name__ == "__main__":
    add_schedule("Complete project", "Work on the final project phase", 1, "2024-05-20")
    for schedule in list_schedules():
        print(schedule)
