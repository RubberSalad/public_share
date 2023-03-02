# python 3 script for generating the Soft deletion payload

reason_description_input = input("Please enter description ex:INCXXX - CORRUPT INVOLVEMENT\n")


import uuid
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()

print('{')
# formatting date and slicing milliseconds to 4 digits
dt_string = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
print(f'"created":"{dt_string[:-3]}",')

UUID_gen = uuid.uuid4()
print(f'"correlation":"{UUID_gen}",')
print(f'"deleted_date":"{dt_string[:-3]}",')
print('"reason_code":"OTHER",')
reason_caps = f'"reason_description":"{reason_description_input}",'
print(reason_caps.upper())
print('"service_id":"ASYLUM_SUPPORT",')
print('"strategy":"SOFT",')
print('"user_id":"ELS_L2",')
print('}')

