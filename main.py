'''
 Name       : main.py
 Author     : AdityaM
 Date       : September 8, 2013
'''

import os
import cPickle as pickle
from dirstruct import DirStruct
'''
A problem that I am facing at the moment is that, I am taking "Applications" and creating 
a tree struture out of that, what I need is, to go within Applications, find the directory 
that contains the collection(different versions of the teh WebApplication). Once that is 
done then, I need to go within those and create a tree for each one of those structures.
Now I have a tree for each of those structures. So for each WebApp(phpBB) I will have as
many trees as there are versions. 
All that I get from the user is an application, Now I need to compare that application, with
everything else in the Directory that I have. The comparison has to be amongst equals, which
means that when considering a Web application, I can only compare it to an application, I will
have to ignore the top directories. So ignore Application, and the ones following that.
Anything else following that should be compared to. 
Steps====
1   Create the a4pplication tree, just the application
2   Create the tre for the entire database.
3   Get the comparison algorithm. 
    1   Now for the comparison, all I need is to have to treat the third child of the root 
        as an independent tree. The parent of this child will be the application example
        PHPBB and the child itself will be the version.
'''
def create_base_tree(directory):
    current = os.path.abspath('.')
    test_app_name = directory #TODO: Should provide the complete path.
    test_app = os.path.join(current, test_app_name)
    try:
        if os.stat('%s.pick'%test_app_name).st_size != 0:
            print 'The structure already exists, and has a non zero size.'

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

create_base_tree('Applications')
