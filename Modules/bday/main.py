# Write code below 💖

import datetime, bday_messages 

today = datetime.date.today()
next_birthday = datetime.date(2027,4,6)

time_different =  next_birthday - today  

if today == next_birthday:
    bday_messages.random_message()
else:
    print(f'My next birthday is {time_different} days away!')