from datetime import datetime
import pytz

'''
program that gets the current local time and tells the user how long it 
is until first break, second break, clock out, or clock in for a desired shift

'''

def do_time_check(shift):
    # print shift name
    shift_name = get_shift_name(shift)
    print('------------------', shift_name ,'Shift ------------------\n')
    
    # get localized time
    x = pytz.timezone("America/Chicago")
    time = datetime.now(x)

    # boolean that will change if the hours are/aren't within the correct shift period
    during_work = True
    
    # set variables according to shift
    set_variables(shift)

    # check if time is before first break, second break, or clock out
    if time.hour < first_break_hour and time.hour >= start_hour:
        var = first_break_hour - time.hour
        var_minutes = 54 - time.minute
        
        if var_minutes < 0:
            var_minutes = 60 + var_minutes
            var -= 1
            
        if var_minutes == 1:
            if var == 0:
                print('It is', var_minutes, 'minute until first break')
            else: 
                print('It is', var ,'hours and', var_minutes ,'minute until first break')

        else:
            if var == 0:
                print('It is', var_minutes, 'minutes until first break')
            else:
                print('It is', var ,'hours and', var_minutes ,'minutes until first break')
            
    # it is first break
    elif time.hour == first_break_hour and time.minute < 10:
        print('It is currently first break')

    # after first break before second break
    elif time.hour < second_break_hour and time.hour >= start_hour:
        # standardize
        if time.minute > 36:
            var = second_break_hour - time.hour
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
            var = second_break_hour - time.hour
            var_minutes = 36 - time.minute
            
            if var_minutes == 1:
                print('It is', var ,'hours and', var_minutes ,'minute until lunch')

            else:
                print('It is', var ,'hours and', var_minutes ,'minutes until lunch')
                
    elif time.hour == second_break_hour and time.minutes < 36:
        var_minutes = 36 - time.minute
        print('It is', var_minutes ,'minutes until lunch')
            
    # it is currently lunch time
    elif time.hour == second_break_hour and time.minutes >= 36:
        print('It is lunch time :)')
        
    # after lunch before clock out
    elif time.hour < end_hour and time.hour >= start_hour:
        # standardize
        if time.minute > 30:
            var = end_hour - time.hour
            var_minutes = 30 - time.minute
            
            if var_minutes < 0:
                var_minutes = 60 + var_minutes
                var -= 1
                
            if var_minutes == 1:
                print('It is', var ,'hours and', var_minutes ,'minute until clock out')

            else:
                print('It is', var ,'hours and', var_minutes ,'minutes until clock out')
            
        # no need to standardize 
        else:
            var = end_hour - time.hour
            var_minutes = 30 - time.minute
            
            if var_minutes == 1:
                print('It is', var ,'hours and', var_minutes ,'minute until clock out')

            else:
                print('It is', var ,'hours and', var_minutes ,'minutes until clock out')
            
    # after lunch before clock out during end hour
    elif time.hour == end_hour and time.minutes < 30:
        var_minutes = time.minute
        print('It is', var_minutes ,'minutes until clock out')
        
    # outside of work hours
    else:
        during_work = False
        print('This shift has not yet started')
        # if it is before midnight
        if time.hour >= start_hour and time.hour < 0:
            # add start time to difference between curr and midnight
            var_hours = 24 - time.hour + start_hour
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
        if time.hour >= 0 and time.hour <= start_hour:
            var_hours = start_hour - time.hour
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
                
    # percentage of work day done
    if during_work:
        # divide current minutes by total minutes
        total_minutes = 480
        
        curr_minutes = time.minute - 30
        curr_hour = time.hour - start_hour
        
        # standardize
        if curr_minutes < 0:
            curr_minutes = 60 + curr_minutes
            curr_hour -= 1
            
        curr_minutes += 60 * curr_hour
        
        curr_minutes = (curr_minutes / total_minutes) * 100
        curr_minutes = round(curr_minutes, 2)
        
        print('You are', curr_minutes,'% through the day')  
        
    # print current time
    time = time.strftime('%H:%M:%S')
    print(time)
    
def get_shift_name(shift):
    if shift == '1':
        return 'First'
    
    elif shift == '2':
        return 'Second'
    
    elif shift == '3':
        return 'Third'
    
    else:
        print('Invalid shift. Please run again')
        quit()
        
    
    
def set_variables(shift):
    # set hour variables according to the shift
    global start_hour, first_break_hour, second_break_hour, end_hour, first_break_minute, second_break_minute
    
    if shift == '1':
        start_hour = 6
        end_hour = 14
        
        first_break_hour = 8
        second_break_hour = 11
        
        first_break_minute = 54
        second_break_minute = 36
        
    if shift == '2':
        start_hour = 14
        first_break_hour = 16
        second_break_hour = 19
        first_break_minute = 54
        second_break_minute = 36
        end_hour = 22
        
    if shift == '3':
        start_hour = 22
        first_break_hour = 0
        second_break_hour = 3
        first_break_minute = 54
        second_break_minute = 36
        end_hour = 6
    
        