month = input('enter month: ').lower().rstrip()
if month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'december':
    print('this month has 31 days')
elif month == 'october':
    print('this month has 31 days and is bambis birthday month!')
elif month == 'february':
    print('this month has 28-29 days')
elif month == 'april' or month == 'june' or month == 'september' or month == 'november':
    print('this month has 30 days')
