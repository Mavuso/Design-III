'''
Fucntion creates unique IDs for each consumption document added.
@Author : L Magudulela
'''
import re

def create_docID(date,building_name,campus_name):
    id = re.sub(r'[^\w]', '', date) + building_name[2:5] + campus_name[2:5] 
    return id