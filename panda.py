import pandas

students = pandas.read_csv('StudentsPerformance.csv')
all = students[students["test preparation course"] == "completed"]
# print(students[students["test preparation course"] == "completed"]["math score"].tail())
print(all[[
    "math score",
    "reading score",
    "writing score"
    ]].sort_values([
        "math score",
        "reading score",
        "writing score"
    ], ascending=False).head()
    )


# print(students.head())
# print(students.tail(3))
# print(students[10:15])

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
