import datetime

import pytz


def reset_command(imei, device):
    if 'Atrak_AX5' in device:
        command = 'AT$REST=1,7'

    elif 'Fox' in device or 'Stepp' in device:
        last_four_reverse = imei[::-1][:4]
        command = '$pfal,sys.security.unlock,"' + last_four_reverse + '"\n$pfal,sys.device.reset'

    elif 'Micron' in device:
        command = 'AT+GTRTO=AIR11,3,,,,,,000B$'

    elif 'Queclink_GL200' in device:
        command = 'AT+GTRTO=gl200,3,,,,,,000B$'

    elif 'Queclink_GL300W' in device:
        command = 'AT+GTRTO=gl300w,3,,,,,,000B$'

    elif 'Queclink_GL300' in device:
        command = 'AT+GTRTO=gl300,3,,,,,,000B$'

    elif 'Queclink_GV500' in device or 'Queclink_GV300' in device:
        command = 'AT+GTRTO=316e66,3,,,,,,FFFF$'

    elif 'USGlobalsat_TR900' in device:
        command = 'GSC,' + imei + ',LH'

    elif 'Ulbotech' in device:
        command = 'RST'

    else:
        command = 'Contact Infospectrum'
    return command


def ping_command(imei, device):
    if 'Atrak_AX5' in device:
        command = 'AT$GPOS=0'

    elif 'Fox' in device or 'Stepp' in device:
        last_four_reverse = imei[::-1][:4]
        command = '$pfal,sys.security.unlock,"' + last_four_reverse + '"\n$PFAL,Sys.GPS.Enable\n$PFAL,Sys.GSM.Enable'

    elif 'Micron' in device:
        command = 'AT+GTRTO=AIR11,0,,,,,,000B$'

    elif 'Queclink_GL200' in device:
        command = 'AT+GTRTO=gl200,0,,,,,,000B$'

    elif 'Queclink_GL300W' in device:
        command = 'AT+GTRTO=GL300W,0,,,,,,000B$'

    elif 'Queclink_GL300' in device:
        command = 'AT+GTRTO=gl300,0,,,,,,000B$'

    elif 'Queclink_GV500' in device or 'Queclink_GV300' in device:
        command = 'AT+GTRTO=316e66,0,,,,,,FFFF$'

    elif 'USGlobalsat_TR900' in device:
        command = 'GSC,' + imei + ',N1'

    elif 'Ulbotech' in device:
        command = 'GPS'

    else:
        command = 'Contact Infospectrum'
    return command


def apn_command(imei, device):
    if 'Atrak_AX5' in device:
        command = 'AT$REST=1,7'

    elif 'Fox' in device or 'Stepp' in device:
        last_four_reverse = imei[::-1][:4]
        command = '$pfal,sys.security.unlock,"' + last_four_reverse + '"\n$pfal,sys.device.reset'

    elif 'Micron' in device:
        command = 'AT+GTRTO=AIR11,3,,,,,,000B$'

    elif 'Queclink_GL200' in device:
        command = 'AT+GTRTO=gl200,3,,,,,,000B$'

    elif 'Queclink_GL300W' in device:
        command = 'AT+GTRTO=gl300w,3,,,,,,000B$'

    elif 'Queclink_GL300' in device:
        command = 'AT+GTRTO=gl300,3,,,,,,000B$'

    elif 'Queclink_GV500' in device or 'Queclink_GV300' in device:
        command = 'AT+GTRTO=316e66,3,,,,,,FFFF$'

    elif 'USGlobalsat_TR900' in device:
        command = 'GSC,' + imei + ','

    elif 'Ulbotech' in device:
        command = 'RST'

    else:
        command = 'Contact Infospectrum'
    return command


def get_date_time_sent():
    date_time = (
        datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('US/Pacific')), '%d.%m.%YT%H:%M:%S')).split('T')
    return date_time[0], date_time[1]


'''
Fox_3G_JSPR_US
Fox_3G_PODSYS_US
FoxLT_JSPR_US
FoxLT_PODSYS_US
SteppIII_JSPR_US
SteppIII_PODSYS_US
SteppII_JSPR_US
SteppII_PODSYS_US

Atrak_AX5_JSPR_US
Atrak_AX5_PODSYS_US

Micron_Prime_1_PODSYS_US

Queclink_GV500_JSPR_US
Queclink_GV500_PODSYS_US

Queclink_GV300_JSPR_US
Queclink_GV300_PODSYS_US

Queclink_GL300W_JSPR_US
Queclink_GL300_PODSYS_US

Queclink_GL200_JSPR_US
Queclink_GL200_PODSYS_US

Ulbotech_JSPR_US
Ulbotech_PODSYS_US

USGlobalsat_TR900_JSPR_US
USGlobalsat_TR900_PODSYS_US

infoTRAK_ISELD9_SPRINT_US

'''
