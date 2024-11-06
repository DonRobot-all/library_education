import datetime

first_date = '02.09.2025'
second_date = '08.09.2025'
# second_date = '02-September-2025'
# third_date = '02 Sep, 25'
first = datetime.datetime.strptime(first_date, '%d.%m.%Y').date()
second = datetime.datetime.strptime(second_date, '%d.%m.%Y').date()
count = 0
while first <= second:
    count += 1
    first += datetime.timedelta(1)
print(count)
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
