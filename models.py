# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account_id = models.AutoField(db_column='Account_ID', primary_key=True)  # Field name made lowercase.
    account_name = models.CharField(db_column='Account_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account_address = models.CharField(db_column='Account_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account_phone = models.CharField(db_column='Account_Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account_fax = models.CharField(db_column='Account_Fax', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primary_contact = models.CharField(db_column='Primary_Contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primary_contact_phone = models.CharField(db_column='Primary_Contact_Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primary_contact_email = models.CharField(db_column='Primary_Contact_Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secondary_contact = models.CharField(db_column='Secondary_Contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secondary_contact_phone = models.CharField(db_column='Secondary_Contact_Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secondary_contact_email = models.CharField(db_column='Secondary_Contact_Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    api_key = models.CharField(db_column='API_Key', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hos_key = models.CharField(db_column='HOS_Key', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zip_code = models.CharField(max_length=250, blank=True, null=True)
    state_code = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ACCOUNT'


class AccountBanner(models.Model):
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    banner_url = models.CharField(db_column='Banner_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    banner_height = models.IntegerField(db_column='Banner_Height', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACCOUNT_BANNER'


class AccountDefaults(models.Model):
    account_id = models.CharField(db_column='Account_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    default_speed_threshold = models.CharField(db_column='Default_Speed_Threshold', max_length=255, blank=True, null=True)  # Field name made lowercase.
    default_distance_unit = models.CharField(db_column='Default_Distance_Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reverse_geocoding_engine = models.CharField(db_column='Reverse_Geocoding_Engine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    default_volume_unit = models.CharField(db_column='Default_Volume_Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    archival_period = models.IntegerField(db_column='Archival_Period', blank=True, null=True)  # Field name made lowercase.
    geofence_radius = models.FloatField(db_column='Geofence_Radius', blank=True, null=True)  # Field name made lowercase.
    support_url = models.CharField(db_column='Support_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_format = models.IntegerField(db_column='Date_Format', blank=True, null=True)  # Field name made lowercase.
    date_seperator = models.CharField(db_column='Date_Seperator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dist_correction = models.FloatField(db_column='Dist_Correction', blank=True, null=True)  # Field name made lowercase.
    health_time = models.IntegerField(db_column='Health_Time', blank=True, null=True)  # Field name made lowercase.
    email_name = models.CharField(db_column='EMail_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='EMail_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alert_name = models.CharField(db_column='Alert_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alert_address = models.CharField(db_column='Alert_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    history_gap_secs = models.IntegerField(db_column='History_Gap_Secs', blank=True, null=True)  # Field name made lowercase.
    idle_time_secs = models.IntegerField(db_column='Idle_Time_Secs', blank=True, null=True)  # Field name made lowercase.
    command_one_label = models.CharField(db_column='Command_One_Label', max_length=45, blank=True, null=True)  # Field name made lowercase.
    command_one = models.CharField(db_column='Command_One', max_length=45, blank=True, null=True)  # Field name made lowercase.
    command_one_status = models.IntegerField(db_column='Command_One_Status', blank=True, null=True)  # Field name made lowercase.
    command_two_label = models.CharField(db_column='Command_Two_Label', max_length=45, blank=True, null=True)  # Field name made lowercase.
    command_two = models.CharField(db_column='Command_Two', max_length=45, blank=True, null=True)  # Field name made lowercase.
    command_two_status = models.IntegerField(db_column='Command_Two_Status', blank=True, null=True)  # Field name made lowercase.
    command_three_label = models.CharField(db_column='Command_Three_Label', max_length=45, blank=True, null=True)  # Field name made lowercase.
    command_three = models.CharField(db_column='Command_Three', max_length=45, blank=True, null=True)  # Field name made lowercase.
    command_three_status = models.IntegerField(db_column='Command_Three_Status', blank=True, null=True)  # Field name made lowercase.
    command_four_label = models.CharField(db_column='Command_Four_Label', max_length=45, blank=True, null=True)  # Field name made lowercase.
    command_four = models.CharField(db_column='Command_Four', max_length=45, blank=True, null=True)  # Field name made lowercase.
    command_four_status = models.IntegerField(db_column='Command_Four_Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACCOUNT_DEFAULTS'


class AccountFeature(models.Model):
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    feature_index = models.IntegerField(db_column='Feature_Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACCOUNT_FEATURE'


class AccountMap(models.Model):
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    map_api = models.CharField(db_column='Map_API', max_length=255, blank=True, null=True)  # Field name made lowercase.
    map_api_key = models.CharField(db_column='Map_API_Key', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACCOUNT_MAP'


class AlertContacts(models.Model):
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact_name = models.CharField(db_column='Contact_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alert_type = models.CharField(db_column='Alert_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    network_operator = models.CharField(db_column='Network_Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone_email = models.CharField(db_column='Phone_Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    speed = models.IntegerField(db_column='Speed', blank=True, null=True)  # Field name made lowercase.
    cell_io = models.IntegerField(db_column='Cell_IO', blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    fence = models.IntegerField(db_column='Fence', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALERT_CONTACTS'


class AlertIndex(models.Model):
    index_type = models.CharField(db_column='Index_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    index_value = models.IntegerField(db_column='Index_Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALERT_INDEX'


class AlertMaster(models.Model):
    alert_index = models.AutoField(db_column='Alert_Index', primary_key=True)  # Field name made lowercase.
    alert_description = models.CharField(db_column='Alert_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALERT_MASTER'


class AlertRules(models.Model):
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    auth_passengers = models.IntegerField(db_column='Auth_Passengers', blank=True, null=True)  # Field name made lowercase.
    active_on_movement = models.IntegerField(db_column='Active_On_Movement', blank=True, null=True)  # Field name made lowercase.
    mofrom = models.FloatField(db_column='MoFrom', blank=True, null=True)  # Field name made lowercase.
    moto = models.FloatField(db_column='MoTo', blank=True, null=True)  # Field name made lowercase.
    tufrom = models.FloatField(db_column='TuFrom', blank=True, null=True)  # Field name made lowercase.
    tuto = models.FloatField(db_column='TuTo', blank=True, null=True)  # Field name made lowercase.
    wefrom = models.FloatField(db_column='WeFrom', blank=True, null=True)  # Field name made lowercase.
    weto = models.FloatField(db_column='WeTo', blank=True, null=True)  # Field name made lowercase.
    thfrom = models.FloatField(db_column='ThFrom', blank=True, null=True)  # Field name made lowercase.
    thto = models.FloatField(db_column='ThTo', blank=True, null=True)  # Field name made lowercase.
    frfrom = models.FloatField(db_column='FrFrom', blank=True, null=True)  # Field name made lowercase.
    frto = models.FloatField(db_column='FrTo', blank=True, null=True)  # Field name made lowercase.
    safrom = models.FloatField(db_column='SaFrom', blank=True, null=True)  # Field name made lowercase.
    sato = models.FloatField(db_column='SaTo', blank=True, null=True)  # Field name made lowercase.
    sufrom = models.FloatField(db_column='SuFrom', blank=True, null=True)  # Field name made lowercase.
    suto = models.FloatField(db_column='SuTo', blank=True, null=True)  # Field name made lowercase.
    cm_1 = models.IntegerField(db_column='CM_1', blank=True, null=True)  # Field name made lowercase.
    cm_2 = models.IntegerField(db_column='CM_2', blank=True, null=True)  # Field name made lowercase.
    cm_3 = models.IntegerField(db_column='CM_3', blank=True, null=True)  # Field name made lowercase.
    cm_4 = models.IntegerField(db_column='CM_4', blank=True, null=True)  # Field name made lowercase.
    cm_5 = models.IntegerField(db_column='CM_5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALERT_RULES'


class AuthorizedFence(models.Model):
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTHORIZED_FENCE'


class BillingStatus(models.Model):
    billing_status = models.CharField(db_column='Billing_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BILLING_STATUS'


class DeviceData(models.Model):
    record_index = models.AutoField(db_column='Record_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    altitude = models.CharField(db_column='Altitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field_strength = models.CharField(db_column='Field_Strength', max_length=2, blank=True, null=True)  # Field name made lowercase.
    distance = models.CharField(db_column='Distance', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    azimuth = models.IntegerField(db_column='Azimuth', blank=True, null=True)  # Field name made lowercase.
    speed_dispatch = models.IntegerField(db_column='Speed_Dispatch', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_DATA'


class DeviceDataView(models.Model):
    record_index = models.AutoField(db_column='Record_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    altitude = models.CharField(db_column='Altitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field_strength = models.CharField(db_column='Field_Strength', max_length=2, blank=True, null=True)  # Field name made lowercase.
    distance = models.CharField(db_column='Distance', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_DATA_VIEW'


class DeviceGroup(models.Model):
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group_index = models.IntegerField(db_column='Group_Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_GROUP'


class DeviceGroupMaster(models.Model):
    group_index = models.AutoField(db_column='Group_Index', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='Group_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_GROUP_MASTER'


class DeviceGroupUser(models.Model):
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.
    group_index = models.IntegerField(db_column='Group_Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_GROUP_USER'


class DeviceQueue(models.Model):
    queue_index = models.AutoField(db_column='Queue_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    command = models.CharField(db_column='Command', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    command_status = models.IntegerField(db_column='Command_Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_QUEUE'


class DeviceRegister(models.Model):
    device_index = models.AutoField(db_column='Device_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device_type_id = models.CharField(db_column='Device_Type_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_no = models.CharField(db_column='SIM_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_No', max_length=20, blank=True, null=True)  # Field name made lowercase.
    device_status = models.CharField(db_column='Device_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asset_no = models.CharField(db_column='Asset_No', max_length=220, blank=True, null=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    driver = models.CharField(db_column='Driver', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gmt_drift = models.CharField(db_column='GMT_Drift', max_length=10, blank=True, null=True)  # Field name made lowercase.
    speed_threshold = models.CharField(db_column='Speed_Threshold', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mileage = models.CharField(db_column='Mileage', max_length=10, blank=True, null=True)  # Field name made lowercase.
    added_on = models.CharField(db_column='Added_On', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billing_status = models.CharField(db_column='Billing_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    time_zone = models.CharField(db_column='Time_Zone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pointer_img = models.CharField(db_column='Pointer_Img', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_REGISTER'


class DeviceStatus(models.Model):
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_STATUS'


class DeviceType(models.Model):
    device_type_id = models.AutoField(db_column='Device_Type_ID', primary_key=True)  # Field name made lowercase.
    device_type = models.CharField(db_column='Device_Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICE_TYPE'


class DriverLog(models.Model):
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.
    driver_status = models.CharField(db_column='Driver_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=20, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DRIVER_LOG'


class DtcMaster(models.Model):
    dtc_index = models.AutoField(db_column='DTC_Index', primary_key=True)  # Field name made lowercase.
    dtc_no = models.CharField(db_column='DTC_No', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dtc_description = models.CharField(db_column='DTC_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DTC_MASTER'


class DvirLog(models.Model):
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dvir_type = models.IntegerField(db_column='DVIR_Type', blank=True, null=True)  # Field name made lowercase.
    dvir_status = models.CharField(db_column='DVIR_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dvir_comments = models.CharField(db_column='DVIR_Comments', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dvir_condition = models.CharField(db_column='DVIR_Condition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dvir_defects = models.CharField(db_column='DVIR_Defects', max_length=20, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DVIR_LOG'


class EmployeeMaster(models.Model):
    employee_id = models.IntegerField(db_column='Employee_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    pr_id = models.CharField(db_column='PR_ID', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE_MASTER'


class FeatureMaster(models.Model):
    feature_index = models.AutoField(db_column='Feature_Index', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    feature = models.CharField(db_column='Feature', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FEATURE_MASTER'


class GeoFence(models.Model):
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=20, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=20, blank=True, null=True)  # Field name made lowercase.
    radius = models.CharField(db_column='Radius', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GEO_FENCE'


class GeoFenceAlerts(models.Model):
    alert_id = models.AutoField(db_column='Alert_ID', primary_key=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=5, blank=True, null=True)  # Field name made lowercase.
    alert_dispatch = models.CharField(db_column='Alert_Dispatch', max_length=2, blank=True, null=True)  # Field name made lowercase.
    trip_index = models.IntegerField(db_column='Trip_Index', blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GEO_FENCE_ALERTS'


class GeoFencePolygon(models.Model):
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GEO_FENCE_POLYGON'


class GeoFencePolygonPoints(models.Model):
    point_id = models.AutoField(primary_key=True)
    geo_fence_polygon_name = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    account_id = models.PositiveIntegerField(db_column='Account_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GEO_FENCE_POLYGON_POINTS'


class GeoFenceUserAlerts(models.Model):
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    account_id = models.CharField(db_column='Account_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GEO_FENCE_USER_ALERTS'


class GfmiA603Stop(models.Model):
    message_index = models.AutoField(db_column='Message_Index', primary_key=True)  # Field name made lowercase.
    unique_id = models.CharField(db_column='Unique_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=50, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=255, blank=True, null=True)  # Field name made lowercase.
    create_epoch_time = models.IntegerField(db_column='Create_Epoch_Time', blank=True, null=True)  # Field name made lowercase.
    reached_epoch_time = models.IntegerField(db_column='Reached_Epoch_Time', blank=True, null=True)  # Field name made lowercase.
    end_epoch_time = models.IntegerField(db_column='End_Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GFMI_A603_STOP'


class GpsHealth(models.Model):
    record_index = models.AutoField(db_column='Record_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fix = models.IntegerField(db_column='Fix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPS_HEALTH'


class HbData(models.Model):
    hb_index = models.AutoField(db_column='HB_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hb = models.CharField(db_column='HB', max_length=40, blank=True, null=True)  # Field name made lowercase.
    hb_status = models.CharField(db_column='HB_Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alert_dispatch = models.CharField(db_column='Alert_Dispatch', max_length=2, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HB_DATA'


class IconSet(models.Model):
    icon_set = models.CharField(db_column='Icon_Set', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ICON_SET'


class IdleData(models.Model):
    idle_index = models.AutoField(db_column='Idle_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alert_dispatch = models.CharField(db_column='Alert_Dispatch', max_length=2, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IDLE_DATA'


class InspectionList(models.Model):
    list_index = models.AutoField(db_column='List_Index', primary_key=True)  # Field name made lowercase.
    element_name = models.CharField(db_column='Element_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INSPECTION_LIST'


class IoData(models.Model):
    io_index = models.AutoField(db_column='IO_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    io = models.CharField(db_column='IO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    io_status = models.CharField(db_column='IO_Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alert_dispatch = models.CharField(db_column='Alert_Dispatch', max_length=2, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IO_DATA'


class IoLabels(models.Model):
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    io = models.CharField(db_column='IO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IO_LABELS'


class IoStatus(models.Model):
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    io = models.CharField(db_column='IO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IO_STATUS'


class Logs(models.Model):
    log_index = models.AutoField(db_column='Log_Index', primary_key=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.
    activity = models.CharField(db_column='Activity', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOGS'


class LrHistory(models.Model):
    lr_index = models.AutoField(db_column='LR_Index', primary_key=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LR_HISTORY'


class MapApi(models.Model):
    api = models.CharField(db_column='API', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAP_API'


class Moum(models.Model):
    message_index = models.AutoField(db_column='Message_Index', primary_key=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    read_by_username = models.CharField(db_column='Read_By_Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=50, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=5, blank=True, null=True)  # Field name made lowercase.
    device_status = models.CharField(db_column='Device_Status', max_length=5, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOUM'


class Mtum(models.Model):
    message_index = models.AutoField(db_column='Message_Index', primary_key=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sent_by_username = models.CharField(db_column='Sent_By_Username', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MTUM'


class MtumCanned(models.Model):
    message_index = models.AutoField(db_column='Message_Index', primary_key=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MTUM_CANNED'


class Notification(models.Model):
    notification_id = models.AutoField(db_column='Notification_ID', primary_key=True)  # Field name made lowercase.
    from_name = models.CharField(db_column='From_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    from_email = models.CharField(db_column='From_EMail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    body = models.CharField(db_column='Body', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    account_id = models.CharField(db_column='Account_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTIFICATION'


class ObdData(models.Model):
    record_index = models.AutoField(db_column='Record_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.
    odometer = models.CharField(db_column='Odometer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    batvolt = models.CharField(db_column='BatVolt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rpm = models.IntegerField(db_column='RPM', blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mf = models.CharField(db_column='MF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    engine_load = models.CharField(db_column='Engine_Load', max_length=20, blank=True, null=True)  # Field name made lowercase.
    throttle = models.CharField(db_column='Throttle', max_length=20, blank=True, null=True)  # Field name made lowercase.
    coolant = models.CharField(db_column='Coolant', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fuel_level = models.CharField(db_column='Fuel_Level', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mil = models.CharField(db_column='MIL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fuel_used = models.CharField(db_column='Fuel_Used', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dtc = models.CharField(db_column='DTC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    alert_dispatch = models.CharField(db_column='Alert_Dispatch', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OBD_DATA'


class ParentAccount(models.Model):
    account_id = models.IntegerField(db_column='Account_ID', primary_key=True)  # Field name made lowercase.
    parent_account_id = models.IntegerField(db_column='Parent_Account_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PARENT_ACCOUNT'


class PostedSpeedData(models.Model):
    ps_index = models.AutoField(db_column='PS_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    posted_speed = models.CharField(db_column='Posted_Speed', max_length=40, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    difference = models.IntegerField(db_column='Difference', blank=True, null=True)  # Field name made lowercase.
    alert_dispatch = models.CharField(db_column='Alert_Dispatch', max_length=2, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POSTED_SPEED_DATA'
        unique_together = (('imei', 'epoch_time'),)


class ProfileFeature(models.Model):
    profile_index = models.IntegerField(db_column='Profile_Index', blank=True, null=True)  # Field name made lowercase.
    feature_index = models.IntegerField(db_column='Feature_Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROFILE_FEATURE'


class ProfileMaster(models.Model):
    profile_index = models.AutoField(db_column='Profile_Index', primary_key=True)  # Field name made lowercase.
    profile_name = models.CharField(db_column='Profile_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROFILE_MASTER'


class RevGeoApi(models.Model):
    api = models.CharField(db_column='API', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REV_GEO_API'


class RouteMaster(models.Model):
    route_index = models.AutoField(db_column='Route_Index', primary_key=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    route_label = models.CharField(db_column='Route_Label', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_geofence = models.CharField(db_column='Start_Geofence', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_geofence = models.CharField(db_column='End_Geofence', max_length=30, blank=True, null=True)  # Field name made lowercase.
    user_defined_distance = models.IntegerField(db_column='User_Defined_Distance', blank=True, null=True)  # Field name made lowercase.
    usps_route_name = models.CharField(db_column='USPS_Route_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usps_trip_name = models.CharField(db_column='USPS_Trip_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usps_trip_leg = models.CharField(db_column='USPS_Trip_Leg', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nassstart = models.CharField(db_column='NASSStart', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nassend = models.CharField(db_column='NASSEnd', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROUTE_MASTER'


class SerialData(models.Model):
    record_index = models.AutoField(db_column='Record_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    altitude = models.CharField(db_column='Altitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='Speed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='Location_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=50, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERIAL_DATA'


class SessionData(models.Model):
    session_index = models.AutoField(db_column='Session_Index', primary_key=True)  # Field name made lowercase.
    iccid = models.CharField(db_column='ICCID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='EventID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eventtype = models.CharField(db_column='EventType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sessionstart = models.CharField(db_column='SessionStart', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sessionend = models.CharField(db_column='SessionEnd', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SESSION_DATA'


class SessionDataView(models.Model):
    session_index = models.AutoField(db_column='Session_Index', primary_key=True)  # Field name made lowercase.
    iccid = models.CharField(db_column='ICCID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='EventID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eventtype = models.CharField(db_column='EventType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sessionstart = models.CharField(db_column='SessionStart', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sessionend = models.CharField(db_column='SessionEnd', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SESSION_DATA_VIEW'


class StateRegister(models.Model):
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=2, blank=True, null=True)  # Field name made lowercase.
    time_zone = models.CharField(db_column='Time_Zone', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gmt = models.CharField(db_column='GMT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dst = models.CharField(db_column='DST', max_length=10, blank=True, null=True)  # Field name made lowercase.
    time_change = models.CharField(db_column='Time_Change', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gas_tax = models.CharField(db_column='GAS_Tax', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diesel_tax = models.CharField(db_column='DIESEL_Tax', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATE_REGISTER'


class SystemConfiguration(models.Model):
    smtp_host = models.CharField(db_column='SMTP_HOST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smtp_port = models.CharField(db_column='SMTP_PORT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    smtp_user_name = models.CharField(db_column='SMTP_USER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smtp_password = models.CharField(db_column='SMTP_PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    debug = models.IntegerField(db_column='DEBUG', blank=True, null=True)  # Field name made lowercase.
    map_api = models.CharField(db_column='Map_API', max_length=255, blank=True, null=True)  # Field name made lowercase.
    map_api_key = models.CharField(db_column='Map_API_Key', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SYSTEM_CONFIGURATION'


class TagAssignment(models.Model):
    tag_index = models.AutoField(db_column='Tag_Index', primary_key=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    driver = models.CharField(db_column='Driver', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tag_id = models.CharField(db_column='Tag_ID', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAG_ASSIGNMENT'


class TestReport(models.Model):
    report_index = models.AutoField(db_column='Report_Index', primary_key=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device_type = models.CharField(db_column='Device_Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stock_type = models.CharField(db_column='Stock_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    physical_condition = models.CharField(db_column='Physical_Condition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    power = models.CharField(db_column='Power', max_length=50, blank=True, null=True)  # Field name made lowercase.
    com_port = models.CharField(db_column='COM_Port', max_length=10, blank=True, null=True)  # Field name made lowercase.
    com_port_comments = models.CharField(db_column='COM_Port_Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gsm_reg = models.CharField(db_column='GSM_Reg', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gsm_reg_comments = models.CharField(db_column='GSM_Reg_Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gps_fix = models.CharField(db_column='GPS_Fix', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gps_fix_comments = models.CharField(db_column='GPS_Fix_Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hardware_ver = models.CharField(db_column='Hardware_Ver', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gprs_state = models.CharField(db_column='GPRS_State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tcp_state = models.CharField(db_column='TCP_State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    server_data = models.CharField(db_column='Server_Data', max_length=10, blank=True, null=True)  # Field name made lowercase.
    io_check = models.CharField(db_column='IO_Check', max_length=10, blank=True, null=True)  # Field name made lowercase.
    io_check_comments = models.CharField(db_column='IO_Check_Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    battery = models.CharField(db_column='Battery', max_length=10, blank=True, null=True)  # Field name made lowercase.
    battery_comments = models.CharField(db_column='Battery_Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    general_comments = models.CharField(db_column='General_Comments', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEST_REPORT'


class TripApi(models.Model):
    trip_api_index = models.AutoField(db_column='Trip_API_Index', primary_key=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trip_id = models.CharField(db_column='Trip_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_date_stamp = models.CharField(db_column='Start_Date_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_time_stamp = models.CharField(db_column='Start_Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_date_stamp = models.CharField(db_column='End_Date_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_time_stamp = models.CharField(db_column='End_Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIP_API'


class TripComments(models.Model):
    comment_id = models.AutoField(db_column='Comment_ID', primary_key=True)  # Field name made lowercase.
    trip_index = models.IntegerField(db_column='Trip_Index', blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIP_COMMENTS'


class TripMaster(models.Model):
    trip_index = models.AutoField(db_column='Trip_Index', primary_key=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    route_index = models.IntegerField(db_column='Route_Index', blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_date_stamp = models.CharField(db_column='Start_Date_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_time_stamp = models.CharField(db_column='Start_Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    actual_start_date_stamp = models.CharField(db_column='Actual_Start_Date_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    actual_start_time_stamp = models.CharField(db_column='Actual_Start_Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_date_stamp = models.CharField(db_column='End_Date_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_time_stamp = models.CharField(db_column='End_Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    actual_end_date_stamp = models.CharField(db_column='Actual_End_Date_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    actual_end_time_stamp = models.CharField(db_column='Actual_End_Time_Stamp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trip_status_id = models.IntegerField(db_column='Trip_Status_ID', blank=True, null=True)  # Field name made lowercase.
    usps_status_id = models.IntegerField(db_column='USPS_Status_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIP_MASTER'


class TripStatus(models.Model):
    trip_status_id = models.AutoField(db_column='Trip_Status_ID', primary_key=True)  # Field name made lowercase.
    trip_status = models.CharField(db_column='Trip_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIP_STATUS'


class TripSummaryData(models.Model):
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    asset_no = models.CharField(db_column='Asset_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    max_speed = models.CharField(db_column='Max_Speed', max_length=20, blank=True, null=True)  # Field name made lowercase.
    avg_speed = models.CharField(db_column='Avg_Speed', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trip_distance = models.CharField(db_column='Trip_Distance', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idel_time = models.CharField(db_column='Idel_Time', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ignition_on_time = models.CharField(db_column='Ignition_On_Time', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odm_distance = models.CharField(db_column='Odm_Distance', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_rpm = models.CharField(db_column='Max_RPM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    avg_rpm = models.CharField(db_column='Avg_RPM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_coolent = models.CharField(db_column='Max_Coolent', max_length=20, blank=True, null=True)  # Field name made lowercase.
    avg_coolent = models.CharField(db_column='Avg_Coolent', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fuel_used = models.CharField(db_column='Fuel_Used', max_length=20, blank=True, null=True)  # Field name made lowercase.
    avg_eng_load = models.CharField(db_column='Avg_Eng_Load', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mileage = models.CharField(db_column='Mileage', max_length=20, blank=True, null=True)  # Field name made lowercase.
    avg_throttle = models.CharField(db_column='Avg_Throttle', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_throttle = models.CharField(db_column='Max_Throttle', max_length=20, blank=True, null=True)  # Field name made lowercase.
    avg_batvolt = models.CharField(db_column='Avg_BatVolt', max_length=20, blank=True, null=True)  # Field name made lowercase.
    max_batvolt = models.CharField(db_column='Max_BatVolt', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_stamp = models.CharField(db_column='Date_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_stamp = models.CharField(db_column='Time_Stamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    epoch_time = models.IntegerField(db_column='Epoch_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIP_SUMMARY_DATA'


class UserAlerts(models.Model):
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alert_index = models.IntegerField(db_column='Alert_Index', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_ALERTS'


class UserMaster(models.Model):
    firstname = models.CharField(db_column='Firstname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_type_id = models.IntegerField(db_column='User_Type_ID', blank=True, null=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='Account_ID', blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_Mail', max_length=180, blank=True, null=True)  # Field name made lowercase.
    alerts = models.CharField(db_column='Alerts', max_length=2, blank=True, null=True)  # Field name made lowercase.
    refresh = models.IntegerField(db_column='Refresh', blank=True, null=True)  # Field name made lowercase.
    map_size = models.IntegerField(db_column='Map_Size', blank=True, null=True)  # Field name made lowercase.
    map_api = models.CharField(db_column='Map_API', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_on = models.CharField(db_column='Created_On', max_length=20, blank=True, null=True)  # Field name made lowercase.
    valid_till = models.CharField(db_column='Valid_Till', max_length=20, blank=True, null=True)  # Field name made lowercase.
    icon_set = models.CharField(db_column='Icon_Set', max_length=20, blank=True, null=True)  # Field name made lowercase.
    klikof = models.CharField(db_column='KlikoF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    klikoadmin = models.CharField(db_column='KlikoAdmin', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_MASTER'


class UserStatus(models.Model):
    user_status = models.CharField(db_column='User_Status', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_STATUS'


class UserType(models.Model):
    user_type_id = models.AutoField(db_column='User_Type_ID', primary_key=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='User_Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_type_description = models.CharField(db_column='User_Type_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_TYPE'


class VehicleInformation(models.Model):
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    make = models.CharField(db_column='Make', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    serial_no = models.CharField(db_column='Serial_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plate = models.CharField(db_column='Plate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vehicle_condition = models.CharField(db_column='Vehicle_Condition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hours = models.IntegerField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    odometer = models.IntegerField(db_column='Odometer', blank=True, null=True)  # Field name made lowercase.
    vmu_location = models.CharField(db_column='VMU_Location', max_length=500, blank=True, null=True)  # Field name made lowercase.
    vmu_wiring = models.CharField(db_column='VMU_Wiring', max_length=500, blank=True, null=True)  # Field name made lowercase.
    base_hub = models.CharField(db_column='Base_Hub', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=500, blank=True, null=True)  # Field name made lowercase.
    starter = models.CharField(db_column='Starter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    next_odometer = models.IntegerField(db_column='Next_Odometer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VEHICLE_INFORMATION'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cities(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class States(models.Model):
    state = models.CharField(max_length=45, blank=True, null=True)
    state_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'
