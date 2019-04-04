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
        command = None
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
        command = None
    return command


def apn_command(imei, device):
    # ================================ Atrak AX5 ================================#
    if 'Atrak_AX5_JSPR_US' in device:
        command = 'AT$GPRS=1,"falcomusa.globalm2m.net","","","us01.infotrak.us",9002,0,5,30,45,0,"0.0.0.0",54088'

    elif 'Atrak_AX5_PODSYS_US' in device:
        command = 'AT$GPRS=1,"data641003","","","us01.infotrak.us",9002,0,5,30,45,0,"0.0.0.0",54088'

    # ============================== Falcom Devices ==============================#

    elif 'FoxLT_JSPR_US' in device or 'Fox_3G_JSPR_US' in device or 'SteppII_JSPR_US' in device or 'SteppIII_JSPR_US' in device:
        last_four_reverse = imei[::-1][:4]
        command = '$pfal,sys.security.unlock,"' + last_four_reverse + '"\n$PFAL,CNF.Set,GPRS.APN=Falcomusa.globalm2m.net'

    elif 'FoxLT_PODSYS_US' in device or 'Fox_3G_PODSYS_US' in device or 'SteppII_PODSYS_US' in device or 'SteppIII_PODSYS_US' in device:
        last_four_reverse = imei[::-1][:4]
        command = '$pfal,sys.security.unlock,"' + last_four_reverse + '"\n$PFAL,CNF.Set,GPRS.APN=data641003'

    # =============================== Micron Devices ==============================#

    elif 'Micron' in device:
        command = 'AT+GTBSI=AIR11,data641003,,,,,,,0002$'

    # =================================== GL200 ===================================#

    elif 'Queclink_GL200_JSPR_US' in device:
        command = 'AT+GTBSI=gl200,falcomusa.globalm2m.net,,,,,,,FFFF$'

    elif 'Queclink_GL200_PODSYS_US' in device:
        command = 'AT+GTBSI=gl200,data641003,,,,,,,FFFF$'


    # ================================== GL300W ===================================#

    elif 'Queclink_GL300W_JSPR_US' in device:
        command = 'AT+GTBSI=gl300w,falcomusa.globalm2m.net,,,falcomusa.globalm2m.net,,,0,FFFF$'

    elif 'Queclink_GL300_PODSYS_US' in device:
        command = 'AT+GTBSI=gl300,data641003,,,data641003,,,0,FFFF$'

    # ================================ GV500/GV300 ================================#

    elif 'Queclink_GV500_JSPR_US' in device or 'Queclink_GV300_JSPR_US' in device:
        command = 'AT+GTBSI=316e66,falcomusa.globalm2m.net,,,,,,,FFFF$'

    elif 'Queclink_GV500_PODSYS_US' in device or 'Queclink_GV300_PODSYS_US' in device:
        command = 'AT+GTBSI=316e66,data641003,,,,,,,FFFF$'

    # =================================== TR900 ===================================#

    elif 'USGlobalsat_TR900_JSPR_US' in device:
        command = 'GSC,' + imei + ',3,0,D1=falcomusa.globalm2m.net,D2=,D3=,DA=02,E0=us01.infotrak.us,E1=9018'

    elif 'USGlobalsat_TR900_PODSYS_US' in device:
        command = 'GSC,' + imei + ',3,0,D1=data641003,D2=,D3=,DA=02,E0=us01.infotrak.us,E1=9018'

    # =================================== T371 ====================================#

    elif 'Ulbotech_PODSYS_US' in device:
        command = 'APN:data641003'

    elif 'Ulbotech_JSPR_US' in device:
        command = 'APN:falcomusa.globalm2m.net'

    # =================================== else ====================================#

    else:
        command = None
    return command


def get_date_time_sent():
    date_time = (
        datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('US/Pacific')), '%d.%m.%YT%H:%M:%S')).split('T')
    return date_time[0], date_time[1]
