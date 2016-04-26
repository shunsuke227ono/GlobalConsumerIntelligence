# coding: utf8

data = [
    { 'name': '田中花子', 'year': 1980, 'score': 58 },
    { 'name': '鈴木一郎', 'year': 2000, 'score': 76 },
    { 'name': '山田太郎', 'year': 1989, 'score': 69 },
    { 'name': '佐藤惠子', 'year': 1992, 'score': 62 },
    { 'name': '石井あや', 'year': 1978, 'score': 71 }
]

# NOTE: This method is answer for assinment 2.
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

# NOTE: This method is answer for assinment 1.
def leap_years(start_year, end_year):
    leap_years = []
    for y in range(start_year, end_year + 1):
        if is_leap_year(y):
            leap_years.append(y)
    return leap_years

def avg(x):
    return 1.0 * sum(x) / len(x)

# NOTE: This method is answer for assinment 3
def average(data):
    scores = []
    for datum in data:
        scores.append(datum['score'])
    return avg(scores)

# NOTE: This method is answer for assinment 3
def average_of_leap_years(data):
    scores = []
    for datum in data:
        if is_leap_year(datum['year']):
            scores.append(datum['score'])
    return avg(scores)

def assinment1():
    years = leap_years(1990, 2200)
    print years

def assinment3():
    ave = average(data)
    leap_ave = average_of_leap_years(data)
    print ave
    print leap_ave

if __name__ == '__main__':
    assinment1()
    assinment3()
