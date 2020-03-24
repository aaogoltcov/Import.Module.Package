from application.db.people import get_employees
from application.salary import calculate_salary

print('Исполнение dirty_main.py:')
get_employees()
calculate_salary()