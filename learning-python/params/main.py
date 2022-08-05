# from datetime import date
# import time

# params = {}

# params['test'] = 'test'
# params['toast'] = 'test'

# print(params)

# today = date.today()

# print(today)

# orario = time.strftime("%H:%M:%S")

# stringa = str(today) + '-' + orario

# print(stringa)

# from datetime import datetime

# # datetime object containing current date and time
# now = datetime.now()
 
# print("now =", now)

# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)

import datetime

from numpy import object_
ora = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print(ora)

object_name='6675/logs/' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print(object_name)
