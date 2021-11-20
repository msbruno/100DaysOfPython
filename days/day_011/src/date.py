import datetime

x = datetime.datetime(2021, 11, 19)
print(x.strftime("%B"))
#November

date_time = datetime.datetime.strptime("19/11/2021", '%d/%m/%Y')
print(type(date_time))
#<class 'datetime.datetime'>
