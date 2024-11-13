# Series
# DataFrame
# s = pandas.Series(data, index)
# s = pandas.Series(range(4), index=['a', 'b', 'c', 'd'])
# print(s)

# print('Выбор одного элемента')
# print(s['a'])
# print('Выбор нескольких элемента')
# print(s[['a', 'b']])
# print('срез')
# print(s[1:])
# print('поэлементное сложнение')
# print(s + s)
# print('фильтрация данных')
# print(s[s > 1])
# s.name = 'Данные'
# s.index.name = 'Индекс'
# print(s)

# students_marks_dict = {
#     "student": ["Студент_1", "Студент_2", "Студент_3"],
#     "math": [5, 3, 4],
#     "physics": [4, 5, 5]}

# s = pandas.DataFrame(students_marks_dict)
# s.index = ['A', 'B', 'C']
# print(s)
# print(s.index)
# print(s.columns)
# print(s.loc['B':])

# d = {
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'd': 40
# }
# r = pandas.Series(d)
# print(r)


import pandas

# students = pandas.read_csv('StudentsPerformance.csv')
# all = students[students["test preparation course"] == "completed"]
# # print(students[students["test preparation course"] == "completed"]["math score"].tail())
# print(all[[
#     "math score",
#     "reading score",
#     "writing score"
#     ]].sort_values([
#         "math score",
#         "reading score",
#         "writing score"
#     ], ascending=False).head()
#     )


# print(students.head())
# print(students.tail(3))
# print(students[10:15])


# import pandas as pd

# # Пример данных (в реальности, вы могли бы загрузить данные через pd.read_csv())
# data = {
#     'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', 
#              '2024-01-03', '2024-01-03', '2024-01-04'],
#     'Product': ['ProductA', 'ProductB', 'ProductA', 'ProductC', 'ProductB', 
#                 'ProductA', 'ProductC', 'ProductA'],
#     'Quantity': [3, 5, 2, 1, 4, 6, 2, 5],
#     'Price': [100, 150, 100, 200, 150, 100, 200, 100],
#     'Total_Sales': [300, 750, 200, 200, 600, 600, 400, 500]
# }

# # Создаём DataFrame
# df = pd.DataFrame(data)

# # 1. Общая сумма продаж по каждому товару
# total_sales_by_product = df.groupby('Product')['Total_Sales'].sum()
# print("Общая сумма продаж по каждому товару:")
# print(total_sales_by_product)

# # 2. Наибольшее количество продаж в день для каждого товара
# max_sales_day = df.groupby('Product')['Quantity'].max()
# print("\nНаибольшее количество продаж в день для каждого товара:")
# print(max_sales_day)

# # 3. Наибольшая выручка по товару
# max_sales_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
# print("\nНаибольшая выручка по товару:")
# print(max_sales_product)

# # 4. Добавляем столбец "Sales_Per_Unit" (средняя цена за единицу товара)
# df['Sales_Per_Unit'] = df['Total_Sales'] / df['Quantity']
# print("\nДанные с добавленным столбцом 'Sales_Per_Unit':")
# print(df)

# # 5. Продажи по месяцам
# df['Date'] = pd.to_datetime(df['Date'])  # Преобразуем колонку Date в datetime
# df['Month-Year'] = df['Date'].dt.to_period('M')  # Извлекаем месяц и год
# sales_by_month = df.groupby('Month-Year')['Total_Sales'].sum()
# print("\nПродажи по месяцам:")
# print(sales_by_month)

# # 6. День с наибольшими продажами (по общей выручке)
# best_day = df.groupby('Date')['Total_Sales'].sum().idxmax()
# print("\nДень с наибольшими продажами:")
# print(best_day)