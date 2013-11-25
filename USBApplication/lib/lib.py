import datetime
from collections import namedtuple

Packet = namedtuple("Packet",[
    'flags','epoch', 'voltage',
    'current', 'period', 'active_power',
    'reactive_power', 'apparent_power',
    'phase_angle', 'power_factor'
    ]
)

def fill_wx_date_with_time(wx_date, wx_time):
    wx_date.SetHour(wx_time.GetHour())
    wx_date.SetMinute(wx_time.GetMinute())
    wx_date.SetSecond(wx_time.GetSecond())
    wx_date.SetMillisecond(wx_time.GetMillisecond()) 
    return wx_date


def wx_datetime_to_python_datetime(wx_datetime):
    return datetime.datetime(
        year=int(wx_datetime.GetYear()),
        month=int(wx_datetime.GetMonth() + 1),
        day=int(wx_datetime.GetDay()),
        hour=int(wx_datetime.GetHour()),
        minute=int(wx_datetime.GetMinute()),
        second=int(wx_datetime.GetSecond()),
        microsecond=int(wx_datetime.GetMillisecond()*1000)
   )
