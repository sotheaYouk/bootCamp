import datetime

def current_date():
    today = datetime.datetime.now()
    
    print(today.date())

    return str(today.date())


current_date()