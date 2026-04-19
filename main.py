from application.db.people import get_employees
from application.salary import calculate_salary
import datetime

if __name__ == "__main__":
    date = datetime.date.today()
    formatted = date.strftime("%d-%m-%Y")
    calculate_salary()
    get_employees()
    print(formatted)
