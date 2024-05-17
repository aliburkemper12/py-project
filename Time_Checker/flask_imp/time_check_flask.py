from datetime import datetime
import pytz
from flask import Flask, render_template, request

'''
program that gets the current local time and tells the user how long it 
is until first break, second break, clock out, or clock in for a desired shift

'''

# does the logic for getting the time check
def do_time_check(shift):
    data = ''
    percent = ''
    
    # get localized time
    x = pytz.timezone("America/Chicago")
    time = datetime.now(x)

    # boolean that will change if the hours are/aren't within the correct shift period
    global during_work
    during_work = True
    
    # set variables according to shift
    set_variables(shift)

    # check if time is before first break, second break, or clock out
    if time.hour < first_break_hour and time.hour > start_hour or (time.hour == start_hour and time.minute > 30) or (time.hour == first_break_hour and time.minute < 54):
        var = first_break_hour - time.hour
        var_minutes = 54 - time.minute
        
        if var_minutes < 0:
            var_minutes = 60 + var_minutes
            var -= 1
            
        data = print_minutes(var_minutes, var, 'first break')
            
    # it is first break
    elif time.hour == first_break_hour and time.minute > 54 or (time.hour == first_break_hour + 1 and time.minute < 10):
        data = 'It is currently first break'

    # after first break before second break
    elif time.hour < second_break_hour and time.hour >= start_hour:
        # standardize
        if time.minute > 36:
            var = second_break_hour - time.hour
            var_minutes = 36 - time.minute
            
            if var_minutes < 0:
                var_minutes = 60 + var_minutes
                var -= 1
                
            data = print_minutes(var_minutes, var, 'lunch')
            
        # no need to standardize 
        else:
            var = second_break_hour - time.hour
            var_minutes = 36 - time.minute
            data = print_minutes(var_minutes, var, 'lunch')
                
    elif time.hour == second_break_hour and time.minute < 36:
        var_minutes = 36 - time.minute
        data = 'It is ' + str(var_minutes) + ' minutes until lunch'
            
    # it is currently lunch time
    elif time.hour == second_break_hour and time.minute >= 36:
        data = 'It is lunch time :)'
        
    # after lunch before clock out
    elif time.hour < end_hour and time.hour >= start_hour:
        # standardize
        if time.minute > 30:
            var = end_hour - time.hour
            var_minutes = 30 - time.minute
            
            if var_minutes < 0:
                var_minutes = 60 + var_minutes
                var -= 1
                
            data = print_minutes(var_minutes, var, 'clock out')
            
        # no need to standardize 
        else:
            var = end_hour - time.hour
            var_minutes = 30 - time.minute
            
            data = print_minutes(var_minutes, var, 'clock out')
            
    # after lunch before clock out during end hour
    elif time.hour == end_hour and time.minute < 30:
        var_minutes = 30 - time.minute
        data = 'It is ' + str(var_minutes) + ' minutes until clock out'
        
    # outside of work hours
    else:
        during_work = False
        data = 'This shift has not yet started'
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
                    
                percent = print_minutes(var_minutes, var_hours, 'clock in')
            else:
                var_minutes = 30 - var_minutes
                
                percent = print_minutes(var_minutes, var_hours, 'clock in')
                
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
                    
                percent = print_minutes(var_minutes, var_hours, 'clock in')
            else:
                var_minutes = 30 - var_minutes
                
                percent =  print_minutes(var_minutes, var_hours, 'clock in')
                
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
        
        percent = 'You are ' + str(curr_minutes) + '%' + ' through the day'
    
    total = [data, percent]
    return total

# returns time as a string to be displayed
def get_time():
    #get current time
    x = pytz.timezone("America/Chicago")
    time = datetime.now(x)
    
    time_hour = time.hour
    if time_hour > 12:
        time_hour = time_hour - 12
    time = str(time_hour) + time.strftime(':%M')
    return str(time)
    
# change shift integer to string for display purposes
def get_shift_name(shift):
    if shift == '1':
        return 'First'
    
    elif shift == '2':
        return 'Second'
    
    elif shift == '3':
        return 'Third'
    
    else:
        return -1
    
# sets the appropriate hours depending on inputted shift
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
        end_hour = 22
        
        first_break_hour = 16
        second_break_hour = 19
        
        first_break_minute = 54
        second_break_minute = 36
        
    if shift == '3':
        start_hour = 22
        end_hour = 6
        
        first_break_hour = 0
        second_break_hour = 3
        
        first_break_minute = 54
        second_break_minute = 36
    
# print function that returns string to be displayed
def print_minutes(var_minutes, var_hours, period):
    result = ''
    if var_minutes == 1:
        if var_hours == 0:
            result = result + 'It is ' + str(var_minutes) + ' minute until ' + str(period)
        elif var_hours == 1:
            result = result + 'It is ' + str(var_hours) + ' hour and ' + str(var_minutes) + ' minute until ' + str(period)
        else:
            result = result + 'It is ' + str(var_hours) + ' hours and ' + str(var_minutes) + ' minute until ' + str(period)

    else:
        if var_hours == 0:
            result = result + 'It is ' + str(var_minutes) + ' minutes until ' + str(period)
        elif var_hours == 1:
            result = result + 'It is ' + str(var_hours) + ' hour and ' + str(var_minutes) + ' minutes until ' + str(period)
        else:
            result = result + 'It is ' + str(var_hours) + ' hours and ' + str(var_minutes) + ' minutes until ' + str(period)
    return result