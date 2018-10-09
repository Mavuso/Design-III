'''
@Author : Lindokuhle Magudulela
function changes string type to date type, very useful when inserting entries on dB

'''
from datetime import datetime

def to_date(date_string):
    datetime_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
    
    return datetime_object
z