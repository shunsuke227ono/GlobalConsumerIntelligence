# coding: utf8

# NOTE: This is the output when this file gets executed.
# $ python assignments.py
# => [Assinment1] Leap years between 1990 and 2200: [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196]
# => [Assignment3] Average in total: 67.200000
# => [Assignment3] Average in leap years: 65.333333

data = [
    { 'name': '田中花子', 'year': 1980, 'score': 58 },
    { 'name': '鈴木一郎', 'year': 2000, 'score': 76 },
    { 'name': '山田太郎', 'year': 1989, 'score': 69 },
    { 'name': '佐藤惠子', 'year': 1992, 'score': 62 },
    { 'name': '石井あや', 'year': 1978, 'score': 71 }
]

# NOTE: This method is answer for assignment2.
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

# NOTE: This method is answer for assignment1.
def leap_years(start_year, end_year):
    leap_years = []
    for y in range(start_year, end_year + 1):
        if is_leap_year(y):
            leap_years.append(y)
    return leap_years

def avg(x):
    return 1.0 * sum(x) / len(x)

# NOTE: This method is answer for assginment3.
def average(data):
    scores = []
    for datum in data:
        scores.append(datum['score'])
    return avg(scores)

# NOTE: This method is answer for assginment3.
def average_of_leap_years(data):
    scores = []
    for datum in data:
        if is_leap_year(datum['year']):
            scores.append(datum['score'])
    return avg(scores)

def assignment1():
    years = leap_years(1990, 2200)
    print "[Assinment1] Leap years between 1990 and 2200: %s" % years

def assignment3():
    ave = average(data)
    leap_ave = average_of_leap_years(data)
    print "[Assignment3] Average in total: %f" % ave
    print "[Assignment3] Average in leap years: %f" % leap_ave

if __name__ == '__main__':
    assignment1()
    assignment3()
