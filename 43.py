#Date time 
#Ex:1
from datetime import datitime , timedifference
current_date = datetime.now()
time_5_days_ago = current_date - timedifference(days = 5)
print("Current date:",current_date)
print("time_5_days_ago:", time_5_days_ago)
#Ex:2
from datetime import datetime , timedifference
today = datetime.now()
yesterday = today - timedifference(day = 1)
tomorrow = today + timedifference(day = 1)
print ("Yesterday:" , yesterday)
print("Today:" , today)
print("Tomorrow:" , tomorrow)
#ex 3
from datetime import datetime 
current_date = datetime.now()
current_date_no_mic = current_date.replace(microsecond=0)
print("current_date:" , current_date)
print("Current date without mic:" ,current_date_no_mic )
#Ex:4
from datetime import datetime
date1 = datetime(2024, 1, 19, 12, 30, 0)
date2 = datetime(2024, 5, 20, 14, 15, 0)
difference_seconds = abs((date2 - date1).total_seconds())
print("Difference in seconds :",difference_seconds)
