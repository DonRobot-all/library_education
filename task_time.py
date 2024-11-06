import datetime
# import calendar

# def get_working_days(start_date, end_date, holidays):
#     ...

# def main():
#     holidays = [
#         datetime.date(2024, 11, 4)
#     ]
#     vacations = [
#         ('02.09.2025', '09.09.2025')
#     ]

# main()

def working_days(start, end, holidays):
    count = 0
    while start <= end:
        if holidays == start:
            start += datetime.timedelta(1)
            continue
        else:
            count += 1
            start += datetime.timedelta(1)
    return count

        

first_date = '02.11.2024'
second_date = '10.11.2024'
first = datetime.datetime.strptime(first_date, '%d.%m.%Y').date()
second = datetime.datetime.strptime(second_date, '%d.%m.%Y').date()
days = working_days(first, second, datetime.date(2024, 11, 4))
print(days)