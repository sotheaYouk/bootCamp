import time

def time_list(second):
    time_list = []
    INVALID = "Invalid integer."

    try:
        second = int(second)
        if second < 0:
            print(INVALID)
            return  []
        
        else:
            while second > 0:
                time_list.append(time.strftime("%X"))
                second -= 1  
                time.sleep(1)

            print(time_list)
            return time_list   
 
    except:
        print(INVALID)
        return  []


time_list(-9)

