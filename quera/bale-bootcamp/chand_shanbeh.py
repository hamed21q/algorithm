import math


month = {
    "Farvardin": 1,
    'Ordibehesht': 2,
    'Khordad': 3,
    'Tir': 4,
    'Mordad': 5,
    'Shahrivar': 6,
    'Mehr': 7,
    'Aban': 8,
    'Azar': 9,
    'Dey': 10,
    'Bahman': 11,
    'Esfand': 12
}

number_of_days = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]

haf = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]

t = 1
# t = int(input())

for _ in range(t):
    roz, mah, hafteh = "23 Khordad jome".split()
    w_roz, w_mah = '18 Azar'.split()

    if month[mah] < month[w_mah]:
        pass
    elif month[mah] > month[w_mah]:
        pass
    else:
        pass
