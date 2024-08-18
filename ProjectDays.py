import calendar
from calendar import month


def main():
    choice = 1
    while choice != 0:
        print("1. Project Planner")
        print("2. Get how many days in a Month")
        print("3. Get day of the week")
        print("0. Exit")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            plan_project()
        elif choice == 2:
            month = int(input("\nEnter month(1-12): "))
            year = int(input("Enter year: "))
            get_days_of_month(month, year)
        elif choice == 3:
            day = int(input("Day: "))
            months = int(input("Month: "))
            years = int(input("Year: "))
            get_day_of_the_week(day, months, years)
        elif choice == 0:
            print("Exit...")
        else:
            print("Invalid choice!")

def plan_project():
    scope = int(input("\nEnter the scope of the project: "))
    hourly_rate = int(input("Enter the hourly wages: "))
    available_employees = int(input("Enter how many employees there are: "))
    total_cost = scope * hourly_rate * available_employees
    total_days = scope // (available_employees * 8) # Assuming every employee works 8 hours a day.
    print(f"\nTotal cost to complete the project: {total_cost}")
    print(f"Total days to complete the project: {total_days}\n")

def get_days_of_month(month, year):
    if month < 1 or month > 12:
        print("The number of month entered is not within range of 1-12!!")
        return None
    days = calendar.monthrange(year, month)[1]
    print(f"Days of the month: {days}\n")
    return days

def leap_year(year):
    return calender.isleap(year)

def get_day_of_the_week(day, month, year):
    if month < 1 or month > 12:
        print("Invalid month!")
        return

    invalid_date = get_days_of_month(month, year)
    if day < 1 or day > invalid_date:
        print(f"Invalid date: {day}.{month}.{year} [The day does not exist!!\n]")
        return

    weekday = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[weekday])

if __name__ == "__main__":
    main()