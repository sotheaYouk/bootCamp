import datetime

def current_time():

    # to get current date and time 
    today = datetime.datetime.now()

    # to filter local time 
    current_time = today.strftime("%X")

    print(current_time)

    return str(current_time)


current_time()