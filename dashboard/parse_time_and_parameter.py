import datetime
import pytz


def date_time_conversion(date_str, time_str):
    '''
    Convert the date and time string into a single data_time object
    :param date_str: Date string
    :param time_str: Time string
    :return: Date_Time object
    '''
    dt = date_str + 'T' + time_str
    date_time = datetime.datetime.strptime(dt, '%d.%m.%YT%H:%M:%S')
    return date_time


def threshold_days_back(dt_obj, threshold_days):
    '''
    Check if the difference between the present time and the date parameter is less than two days
    :param dt_obj: Date_Time object
    :return: Boolean True/False based on the time-delta
    '''
    now = datetime.datetime.strptime(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('%d.%m.%YT%H:%M:%S'),
                                     '%d.%m.%YT%H:%M:%S')
    print(now)
    diff = now - dt_obj
    return diff.days > datetime.timedelta(days=int(threshold_days)).days
