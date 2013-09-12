'''
 Name		: main.py
 Author		: AdityaM
 Date		: September 8, 2013
'''

import os
import time

from dirstruct import DirStruct

millis = round(time.time())
current = os.path.abspath('.')
app_path = os.path.join(current, 'Applications')
new_struct = DirStruct(app_path)
print 'The total took %d seconds' %(time.time()- millis)
