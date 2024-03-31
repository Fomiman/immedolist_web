from controllers import add_schedule, list_schedules

def display_menu():
    print("1. Add Schedule")
    print("2. List Schedules")
    print("3. Exit")
    choice = input("Choose an option: ")
    return choice

def main_loop():
    while True:
        choice = display_menu()
        
        if choice == "1":
            title = input("Title: ")
            details = input("Details: ")
            priority = input("Priority (1-5): ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            add_schedule(title, details, priority, due_date)
            
        elif choice == "2":
            schedules = list_schedules()
            for schedule in schedules:
                print(f"{schedule.id}. {schedule.title} (Priority: {schedule.priority}, Due: {schedule.due_date})")
                
        elif choice == "3":
            print("Exiting...")
            break

if __name__ == "__main__":
    main_loop()
