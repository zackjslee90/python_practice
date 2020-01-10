import pandas as pd

"""
# df = pd.read_csv('/Users/zackjslee/Desktop/pythonproject/friend_list.csv')
# print(df.head(2))

# 파일이 csv가 아니고 탭으로 구분되어있으면
# df = pd.read_csv('data/friend_list_tab.txt', delimiter = '/t')

# 파일에 헤더가 없을때
# df = pd.read_csv('data/friend_list.txt', header = None)
# 헤더 집어넣기
# df.columns = ['name', 'age', 'job']
# df = pd.read_csv('data/friend_list_no_head.csv', header = None, names = ['name', 'age', 'job']

# friend_dict_list = [
#    {'name': 'John', 'age': 25, 'job': 'student'},
#    {'name': 'Nate', 'age': 30, 'job': 'teacher'}
#]
# df = pd.DataFrame(friend_dict_list)
# df = df[['name', 'age', 'job']]
# print(df.head())

# dictionary 사용해서 Header 알파벳 순서대로 나오게하기
from collections import OrderedDict
friend_ordered_dict = OrderedDict(
    [
        ('name', ['John', 'Nate']),
        ('age', ['25', '30']),
        ('job', ['student', 'teacher'])
    ]
)
df = pd.DataFrame.from_dict(friend_ordered_dict)
print(df.head())
"""

"""
# 리스트 만들기 (Column header 따로 넣기)
friend_list = [
    ['John', 20, 'student'],
    ['Nate', 30, 'teacher']
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns = column_name)
print(df.head())
"""

"""
# 리스트에 헤더까지 만들어서 넣기
friend_lists = [
    ['name', ['John', 'Nate']],
    ['age', [20, 30]],
    ['job', ['student', 'teacher']]
]
df = pd.DataFrame.from_items(friend_lists)
print(df.head())
"""

"""
# csv 파일로 저장하기
friend_lists = [
    {'name': 'Jone', 'age': 20, 'job': 'student'},
    {'name': 'Jenny', 'age': 30, 'job': None},
    {'name': 'Nate', 'age': 30, 'job': 'teacher'}
]

df = pd.DataFrame(friend_lists)
df = df[['name', 'age', 'job']]
# 첫번째 컬럼 넣고 싶지않으면 index = False, 헤더 없이 저장하고싶으면 header = False
df.to_csv('friends.csv', index = False, header = False, na_rep = '-')
print(df.head())


# 행 과 열 필터하기

friend_list = [
    ['name', ['John', 'Jenny', 'Nate']],
    ['age', [20, 30, 30]],
    ['job', ['student', 'developer', 'teacher']]
]
df = pd.DataFrame.from_items(friend_list)

# index 0, 2 번만 선택
# df = df.loc[[0,2]]
# print(df.loc[[0, 2]])

# row 선택 (by column condition
df[df.age > 25] # 나이가 25 이상
df.query('age>25') # 나이가 25 이상
df[(df.age > 25) & (df.name == 'Nate')] # 나이가 25 이상이면서 이름이 Nate

# filter column by index
friend_list = [
    ['John', 20, 'student'],
    ['Jenny', 30, 'developter'],
    ['Nate', 30, 'teacher']
]
df = pd.DataFrame.from_records(friend_list)
df.iloc[0:3,0:2] # 첫번째 : > row 나타냄. >> row 전부를 가져와라

# filter column by column name
df = pd.read_csv('/Users/zackjslee/Desktop/pythonproject/friend_list_no_head.csv', header = None, names=['name', 'age', 'job'])
df_filtered = df[['name', 'age']] # column 이름이 name과 age만 불러오기
df.filter(items=['age', 'job']) # column 이름이 age와 job만 불러오기
df.filter(like='a', axis=1) # axis=1 >> 컬럼이름에 a가 들어간것들만 찾기
print(df.filter(regex='e$', axis=1)) # 컬럼이름이 e로 끝나는 것 찾기
"""

""" # 데이타 프레임에서 Drop 시키는방법
friends = [{'age': 15, 'job': 'student'},
           {'age': 25, 'job': 'developer'},
           {'age': 30, 'job': 'teacher'}]
df = pd.DataFrame(friends,
                  index = ['John', 'Jenny', 'Nate'],
                  columns = ['age', 'job'])
# df = df.drop(['John', 'Nate']) # index 입력해서 해당 row 삭제하기
# df.drop(['John', 'Nate'], inplace = True) # inplace 사용해서 삭제하기

friends = [{'name': 'John', 'age': 15, 'job': 'student'},
           {'name': 'Ben', 'age': 25, 'job': 'developer'},
           {'name': 'Jenny', 'age': 30, 'job': 'teacher'}]
df = pd.DataFrame(friends,
                  columns = ['name', 'age', 'job'])

# df = df.drop(df.index[[0,2]]) # row의 index로 삭제하기 (여러개의 index)
# df = df[df.age > 20] # column의 value에 따라서 드랍시키기
# df = df.drop('age', axis=1) #컬럼중에서 age를 드랍시키기
# df.drop('age', axis=1, inplace = True)

print(df.head())
"""

"""
# 행, 열 생성 및 수정하기
friend_dict_list = [{'name': 'Jone', 'midterm': 95, 'final': 85},
                    {'name': 'Jenny', 'midterm': 85, 'final': 80},
                    {'name': 'Nate', 'midterm': 30, 'final': 10}]
df = pd.DataFrame(friend_dict_list,
                  columns=['name', 'midterm', 'final'])
# df['salary'] = 0  # Salary column 생성

# numpy 사용해서 Column 값 추가하기
# import numpy as np
# df['salary'] = np.where(df['job'] != 'student', 'yes', 'no')

df['total'] = df['midterm'] + df['final']
df['avg'] = df['total'] / 2

# python for 사용해서 grade 자동으로 생성하기
grades = []
for row in df['avg']:
    if row >= 90:
        grades.append('A')
    elif row >= 80:
        grades.append('B')
    else:
        grades.append('F')
df['grade'] = grades

# python def 사용해서 grade Pass or Fail 생성하기
def pass_or_fail(row):
    if row != 'F':
        return "Pass"
    else:
        return "Fail"

df.grade = df.grade.apply(pass_or_fail)

print(df.head())
"""


"""
### def 사용해서 날짜중에 연도만 가져오기
date_list = [
    {
        'yyyy-mm-dd' : '2000-06-27'
    },
    {
        'yyyy-mm-dd': '2007-10-27'
    }
]

df = pd.DataFrame(date_list, columns = ['yyyy-mm-dd'])

def extract_year(row):
    return row.split('-')[0]
df['year'] = df['yyyy-mm-dd'].apply(extract_year)

print(df.head())
"""

"""
### 열 추가하는 방법
friend_dict_list = [{'name': 'Jone', 'midterm': 95, 'final': 85},
                    {'name': 'Jenny', 'midterm': 85, 'final': 80},
                    {'name': 'Nate', 'midterm': 30, 'final': 10}]
df = pd.DataFrame(friend_dict_list,
                  columns=['name', 'midterm', 'final'])

df2 = pd.DataFrame([
    ['Ben', 50, 50]
], columns = ['name', 'midterm', 'final'])
print(df2)

df.append(df2, ignore_index = True)

print(df)
"""


"""
### 8) 데이터 그룹 만들기 (group by)
student_list = [
    {'name': 'John', 'major': "Computer Science", 'sex': 'male'},
    {'name': 'Nate', 'major': "Computer Science", 'sex': 'male'},
    {'name': 'Abraham', 'major': "Physics", 'sex': 'male'},
    {'name': 'Brian', 'major': "Psychology", 'sex': 'male'},
    {'name': 'Janny', 'major': "Economics", 'sex': 'female'},
    {'name': 'Yuna', 'major': "Economics", 'sex': 'female'},
    {'name': 'Jennifer', 'major': "Computer Science", 'sex': 'female'},
    {'name': 'Edward', 'major': "Computer Science", 'sex': 'male'},
    {'name': 'Zara', 'major': "Psychology", 'sex': 'female'},
    {'name': 'Wendy', 'major': "Economics", 'sex': 'female'},
    {'name': 'Sera', 'major': "Psychology", 'sex': 'female'}
]

df = pd.DataFrame(student_list, columns = ['name', 'major', 'sex'])
## major별로 구분해서 for 사용해서 보기쉽게 만들기
groupby_major = df.groupby('major')
for name, group in groupby_major:
    print(name + " : " + str(len(group)))
    print(group)
    print()

## major 총 몇개있는지 보기
df_major_cnt = pd.DataFrame( {'count': groupby_major.size()}).reset_index()
print(df_major_cnt)

## 성별로 구분해서 for 이용해서 보기쉽게 만들기
groupby_sex = df.groupby('sex')
for name, group in groupby_sex:
    print(name + " : " + str(len(group)))
    print(group)
    print()
"""


### 중복데이터 삭제하기 (drop duplicates)
student_list = [
    {'name': 'John', 'major': "Computer Science", 'sex': 'male'},
    {'name': 'Nate', 'major': "Computer Science", 'sex': 'male'},
    {'name': 'Abraham', 'major': "Physics", 'sex': 'male'},
    {'name': 'Brian', 'major': "Psychology", 'sex': 'male'},
    {'name': 'Janny', 'major': "Economics", 'sex': 'female'},
    {'name': 'Yuna', 'major': "Economics", 'sex': 'female'},
    {'name': 'Jennifer', 'major': "Computer Science", 'sex': 'female'},
    {'name': 'Edward', 'major': "Computer Science", 'sex': 'male'},
    {'name': 'Zara', 'major': "Psychology", 'sex': 'female'},
    {'name': 'Wendy', 'major': "Economics", 'sex': 'female'},
    {'name': 'Sera', 'major': "Psychology", 'sex': 'female'}
]

df = pd.DataFrame(student_list, columns = ['name', 'major', 'sex'])

print(df)
