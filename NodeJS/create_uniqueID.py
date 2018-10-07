'''
Fucntion creates unique IDs for each consumption document added.
@Author : L Magudulela
'''
import re

def create_docID(date,building_id):
    date = "2013-08-08 13:15"
    id = re.sub(r'[^\w]', '', date) + building_id
    return id