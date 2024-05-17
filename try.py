#!/usr/bin/python3

#import pendulum
#
#n = pendulum.now()
#
#print(n)

#import datetime
#from datetime import datetime
#strptime = datetime.strptime
#
#e = strptime("6 PM", "")
#
#print(e)

# function parameter/result interface:
#
# time: string of the remote time
#
# timezone: timezone of remote time to parse time in

def show_remote_time(time, timezone):
    result_str = remote_time_in_local_timezone(time, timezone)

    return result_str

