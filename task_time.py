import datetime
import calendar

def get_working_days(start_date, end_date, holidays):
    count = 0
    while start_date <= end_date:
        if start_date not in holidays:
            count += 1
    

        # if start_date.weekday() < 5: #and start_date not in holidays:
        #     count += 1
        # start_date += datetime.timedelta(days=1)

def main():
    holidays = [
        datetime.date(2024, 11, 4)
    ]
    vacations = [
        ('02.09.2025', '09.09.2025')
    ]
    # тут ввод данных и вызов функции get_working_days
    first = datetime.datetime.strptime(input(), '%d.%m.%Y').date()
    second = datetime.datetime.strptime(input(), '%d.%m.%Y').date()
    get_working_days(first, second, holidays)

main()
