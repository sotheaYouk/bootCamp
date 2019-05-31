import datetime

def date_time():

    current_date = datetime.datetime.now()
    today = current_date.date()
    current_time = current_date.strftime("%X")
    current_date = str(today) + " " + str(current_time)

    print(current_date)

    return current_date

date_time()
