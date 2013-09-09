'''
 Name		: main.py
 Author		: AdityaM
 Date		: September 8, 2013
'''

import os

from dirstruct import DirStruct

current = os.path.abspath('.')
app_path = os.path.join(current, 'Applications')
new_struct = DirStruct(app_path)
