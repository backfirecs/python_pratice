"""

计算给定的年月日是哪一天

Version:1.0
Author:chaishuai

"""

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 or (year % 3200 == 0 and year % 172800):
        return True
    return False

def which_day(year, month, day):
    big_month = [1, 3, 5, 7, 8, 10, 12]
    day_counter = 0
    for x in range(1, month):
        if x in big_month:
            day_counter += 31
        elif x == 2:
            day_counter += 29 if is_leap_year(year) else 28
        else:
            day_counter +=  30
    day_counter += day
    return day_counter

def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))

if __name__ == '__main__':
    main()