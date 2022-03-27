import datetime

colors = {'clear':'\033[m',
          'red':'\033[31m',
          'green':'\033[32m',
          'blue':'\033[34m',
          'yellow':'\033[33m',
          'purple':'\033[35m'}

born = int(input('{}When were you born? {}'.format(colors['purple'], colors['clear'])))
today = datetime.date.today().year
age = today - born

if age <= 9:
    print('The athlete has {} years old and is in the category "Little".'.format(age))
elif 14 >= age > 9:
    print('The athlete has {} years old and in in the category "Childish".'.format(age))
elif 19 >= age > 14:
    print('The athlete has {} years old and is in the category "Junior".'.format(age))
elif age >= 20:
    print('The athlete has {} years old and is in the category "Senior".'.format(age))