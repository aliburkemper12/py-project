'''
program that gets the current local time and tells the user how long it 
is until first break, second break, clock out, or clock in

'''

from datetime import datetime
import pytz

# get localized timezone
x = pytz.timezone("America/Chicago")
time = datetime.now(x)

# check if time is before first break, second break, or clock out
if time.hour < 9:
    var = 9 - time.hour
    var_minutes = 0 - time.minute
    
    if var_minutes < 0:
        var_minutes = 60 + var_minutes
        var -= 1
        
    if var_minutes == 1:
        print('It is', var ,'hours and', var_minutes ,'minute until first break')

    else:
        print('It is', var ,'hours and', var_minutes ,'minutes until first break')
        
elif time.hour == 9 and time.minutes < 15:
    print('It is currently first break')

# after first break before second break
elif time.hour < 11:
    # standardize
    if time.minute > 36:
        var = 11 - time.hour
        var_minutes = 36 - time.minute
        
        if var_minutes < 0:
            var_minutes = 60 + var_minutes
            var -= 1
            
        if var_minutes == 1:
            print('It is', var ,'hours and', var_minutes ,'minute until lunch')

        else:
            print('It is', var ,'hours and', var_minutes ,'minutes until lunch')
           
    # no need to standardize 
    else:
        var = 11 - time.hour
        var_minutes = 36 - time.minute
        
        if var_minutes == 1:
            print('It is', var ,'hours and', var_minutes ,'minute until lunch')

        else:
            print('It is', var ,'hours and', var_minutes ,'minutes until lunch')
            
elif time.hour == 11 and time.minutes < 36:
    var_minutes = 36 - time.minute
    print('It is', var_minutes ,'minutes until lunch')
        
elif time.hour == 11 and time.minutes >= 36:
    print('It is lunch time :)')
    
elif time.hour < 14:
     # standardize
    if time.minute > 30:
        var = 14 - time.hour
        var_minutes = 30 - time.minute
        
        if var_minutes < 0:
            var_minutes = 60 + var_minutes
            var -= 1
            
        if var_minutes == 1:
            print('It is', var ,'hours and', var_minutes ,'minute until lunch')

        else:
            print('It is', var ,'hours and', var_minutes ,'minutes until lunch')
           
    # no need to standardize 
    else:
        var = 14 - time.hour
        var_minutes = 30 - time.minutes
        
        if var_minutes == 1:
            print('It is', var ,'hours and', var_minutes ,'minute until lunch')

        else:
            print('It is', var ,'hours and', var_minutes ,'minutes until lunch')
        
elif time.hour == 14 and time.minutes < 30:
    var_minutes = time.minute
    print('It is', var_minutes ,'minutes until clock out')
    
else:
    print('You are not currently scheduled!')
    # if it is before midnight
    if time.hour >= 14 and time.hour < 0:
        # add 6 hours and 30 minutes onto difference between curr and midnight
        var_hours = 24 - time.hour + 6
        var_minutes = time.minutes
        
        # standardize
        if var_minutes > 30:
            var_minutes = 30 - var_minutes
        
            if var_minutes < 0:
                var_minutes = 60 + var_minutes
                var_hours -= 1
                
            if var_minutes == 1:
                print('It is', var_hours ,'hours and', var_minutes ,'minute until clock in')

            else:
                print('It is', var_hours ,'hours and', var_minutes ,'minutes until clock in')
        else:
            var_minutes = 30 - var_minutes
            
            if var_minutes == 1:
                print('It is', var_hours ,'hours and', var_minutes ,'minute until clock in')

            else:
                print('It is', var_hours ,'hours and', var_minutes ,'minutes until clock in')
            
    # between midnight and clock in
    if time.hour >= 0 and time.hour < 6:
        var_hours = time.hour
        var_minutes = time.minute
        
        # standardize
        if var_minutes > 30:
            var_minutes = 30 - var_minutes
        
            if var_minutes < 0:
                var_minutes = 60 + var_minutes
                var_hours -= 1
                
            if var_minutes == 1:
                print('It is', var_hours ,'hours and', var_minutes ,'minute until clock in')

            else:
                print('It is', var_hours ,'hours and', var_minutes ,'minutes until clock in')
        else:
            var_minutes = 30 - var_minutes
            
            if var_minutes == 1:
                print('It is', var_hours ,'hours and', var_minutes ,'minute until clock in')

            else:
                print('It is', var_hours ,'hours and', var_minutes ,'minutes until clock in')
            

time = time.strftime('%H:%M:%S')

print(time)

    