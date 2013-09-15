'''
 Name		: main.py
 Author		: AdityaM
 Date		: September 8, 2013
'''

import os
import cPickle as pickle
from dirstruct import DirStruct

current = os.path.abspath('.')
test_app_name = 'Applications'
test_app = os.path.join(current, test_app_name)
try:
	if os.stat('%s.pick' %test_app_name).st_size != 0:
		print 'The structure already exists, and has a non zero size'
	'''
	Getting the data structure back from the file, and testing it.
	'''
	tree_struct = pickle.load(open('%s.pick' %test_app_name, 'rb'))
	tree_struct.recurse_tree('2.txt')
except:
	tree = DirStruct(test_app)
	tree.recurse_tree('1.txt')
	pick  = pickle.dump(tree, open('%s.pick' %test_app_name, 'wb'))
	print 'The structure has been created'
