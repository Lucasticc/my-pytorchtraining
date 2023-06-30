c = 0
for i in range(1,2021):
    i = str(i)
    l = list(i)
    for j in l:
        if j == '2':
            c += 1
print(c)

import datetime
star = datetime.date(2000,1,1)
end = datetime.date(2020,10,1)
count = 0
a = datetime.timedelta(days=1)
while star<end:
    if star.day == 1 or star.weekday() == 0:
        count += 2
    else:
        count += 1
    star += a
print(count)