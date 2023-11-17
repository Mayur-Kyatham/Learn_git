# function's
def is_leap(year):
    leap = False
    leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return leap
// write a function // 
year = int(input())
print(is_leap(year))
