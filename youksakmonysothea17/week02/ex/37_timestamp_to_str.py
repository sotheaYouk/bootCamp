from datetime import datetime

def timestamp_to_str(my_timestamp):

    try:
        my_timestamp = int(my_timestamp)
        current_date = datetime.fromtimestamp(my_timestamp)
        print(current_date)
       
        return current_date
    
    except:
        print("Your timestamp is not valid.")
        
        return 0
            

timestamp_to_str("1623646780")







