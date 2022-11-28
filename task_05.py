#  Task - Done!
from datetime import datetime, timedelta


def date_in_future(date_day_future: int) -> str:
    if isinstance(date_day_future, int):
        time_future = datetime.now() + timedelta(days=date_day_future)
        return time_future.strftime('%d-%m-%Y %H:%M:%S')
    else:
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


#print(date_in_future([]))

