import datetime
import calendar

# date
# time
# datetime

somedate = datetime.date(2012, 9, 1)
print(somedate)

today = datetime.date.today()
print(today)

print(f'Сегодня {today.year}, месяц {today.month}, {today.day}, день недели {today.weekday()}')


timer = datetime.time()
print(timer)

timer = datetime.time(16, 25)
print(timer)

timer = datetime.time(16,25,45)
print(timer)


day = datetime.datetime(2023, 12, 10, 12,15,15)
print(day)

today = datetime.datetime.now()
print(today)
print(today.date())
print(today.time())
print(today.day, today.minute)


test = '22.07.2012'
str_to_obj = datetime.datetime.strptime(test, '%d.%m.%Y')
print(str_to_obj)

test = '10.11.2024 12:30:30'
str_to_obj = datetime.datetime.strptime(test, '%d.%m.%Y %H:%M:%S')
# str_to_obj += datetime.timedelta(days=1)
print(str_to_obj.weekday())
print(str_to_obj.day)
print(str_to_obj.month)


    # %d: день месяца в виде числа
    # %m: порядковый номер месяца
    # %y: год в виде 2-х чисел
    # %Y: год в виде 4-х чисел
    # %H: час в 24-х часовом формате
    # %M: минута
    # %S: секунда










# first_date = '02.09.2025'
# second_date = '08.09.2025'
# # second_date = '02-September-2025'
# # third_date = '02 Sep, 25'
# first = datetime.datetime.strptime(first_date, '%d.%m.%Y').date()
# second = datetime.datetime.strptime(second_date, '%d.%m.%Y').date()
# count = 0
# while first <= second:
#     count += 1
#     first += datetime.timedelta(1)
# print(count)
# all_time = second - first
# str_all_time = all_time.days
# print(str_all_time)
# second = datetime.datetime.strptime(second_date, '%d-%B-%Y')
# third = datetime.datetime.strptime(third_date, '%d %b, %y')
# print(first)
# print(second)
# print(third)
# time = datetime.datetime.now()
# day_of_the_month = time.strftime('%d')
# day_of_the_week = time.strftime('%A')
# month = time.strftime('%B')
# year = time.strftime('%Y')
# print(f'{day_of_the_month}, \n{day_of_the_week}, \n{month}, \n{year}')
# print(time)

# дата имеет формат DD.MM.YYYY. 
# Чтобы передать информацию об этом в метод мы используем 
# следующие обозначения:

#     %d — день месяца в виде десятичного числа;
#     %m — номер месяца;
#     %Y — год с указанием века;
