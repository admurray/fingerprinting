'''
 Name       : dirstruct.py
 Author     : AdityaM
 Date       : September 8, 2013
'''

import os
import sys
import zipfile
import cPickle as pickle

extensions = ['.zip', '.tar.gz']

class FileStruct:
    def __init__(self, file_path):
        if os.path.isdir(file_path):
            print 'This is not a file and may be a directory'
            print 'Something might be wrong with the directory base'
            print 'case, where the call to create the FileStruct is'
            print 'being made'
        self.file_path = file_path
        self.type = 'file'
        self.file_name = self.file_path[str.rfind(self.file_path, '\\')+1:]
        with open('test.txt', 'a') as test:
            test.write('%s\n'%self.file_name)

    def recurse_tree(self, filename):
        with open(filename, 'a') as test:
            test.write('%s  : FILE\n'%self.file_path)
        return

class DirStruct:

    '''
    In this class my main aim is to create a structure that can store
    a complete directory, with other directories and files. Unlike a
    file system. I just wish to have information regarding the file
    system and not the entire system. So I would want to store the
    filename, its parent and a Filestruct of each directory within it,
    How could I do that. I would have a main directory stored as a
    filestruct. Now this filestruct may have other filestructs within it.
    ===
    Another thing that did come to mind was whether to have a different
    class for File and a different one for directory and then a directory
    contains a list of directories and files. But at the moment I see
    no benefit o having them as different, so I have just se a flag
    representing whether on is a directory or a file.

    I decided to create a new class called FileStruct, beacuse, it
    offers me a convinient way to set a base case, and not worry about
    dealing with a directory, when wanting to set a base case.
    ===

    @pre -  The __init__ method can be called only on a directory.
    '''

    def __init__(self, dir_path):
        self.file_path =  dir_path
        # Type is a python method/type whih I am trying to overwrite
        # If this is a bad practice. I will change it to something else.
        self.file_name = self.file_path[str.rfind(self.file_path, '\\')+1:]
        self.type = 'dir'
        #Check if the path entered is a directory
        self.is_dir = os.path.isdir(self.file_path)
        with open('test.txt', 'a') as test:
            test.write('%s\n'%self.file_path)
        if not self.is_dir:
            print 'This is not a valid directory. A file structure'
            print 'can only be built starting at a directory, please,'
            print 'confirm that you have entered the name correctly.'
            print 'You may do down a directory and retry.'
            print 'If you think that this may be a bug, please report'
            print 'it to adityamurray@yahoo.com'

        # This contains all the files that are in the directory.
        self.children = []
        number_of_files = 0
        
        self.__create_tree__()

    def __create_tree__(self):
        '''
        In order to create a tree I need to go through, each file/dir
        in a directoy and call DirStruct on each directory that I come
        accross. This will set_up the tree for that directory, 
        this tree is then inserted into the parent.children list.
        TODO: Try to use os.walk() instead of os.listdir, in my opinion
        that would be far more efficient, although, even in that case,
        I will have to loop through each element so I don't know if that
        will be any more efficient.
        '''
        all_files = os.listdir(self.file_path)
        self.number_of_files = len(all_files)
        for each in all_files:
            child_path = os.path.join(self.file_path,each )
            zip_path, extension = os.path.splitext(child_path)
            if os.path.isdir(child_path):
                '''
                If the child is a directory instantiate and add to the
                list of children
                '''
                self.children.append(DirStruct(child_path))
            elif extension in extensions:
                '''
                TODO: For extensions like 'tar' and 'zip' do not
                extract, but go through the tar and zip to form the tree
                and store the data structure so created using that pickle
                thingi that Jesse and Tyson used.
                '''
                if extension == '.zip':
                    zipped = zipfile.ZipFile(child_path)
                    zipped.extractall(zip_path)
                    print 'Removing : %s' % child_path
                    os.remove(child_path)
            else:
                '''
                This here is the base case that deals with the files,
                and not the directories.
                I could give the names the same named variable in both
                the File and the directory struct to make printing easier,
                but it might be better to leave both differet so as to facilitate
                debugging.
                '''
                self.children.append(FileStruct(child_path) )
    
    def recurse_tree(self, filename):
        '''
        This method should re-curse over every file and directory stored in the
        tree. I could have it create a in-order, pre-order or a post-order list
        so that iterating becomes easier. I would rather have a way to create a
        generic traversal and have an action defined for it in the form of a function
        which lets say takes a node (file or directory) and acts on that accordingly.
        That is something that I can build up on. For now I will just do a simple
        traversal. With a built in call to print the name of the file or directory.
        '''
        if self.type == 'file':
            with open(filename, 'a') as test:
                test.write('%s  : FILE\n'%self.file_path)
            return
        elif self.type == 'dir' and len(self.children) == 0:
            with open(filename, 'a') as test:
                test.write('%s  : EMPTY_DIR\n'%self.file_path)
            return
        else:
            with open(filename, 'a') as test:
                test.write('%s  : COMPUTING\n'%self.file_path)
            for each in self.children:
                each.recurse_tree(filename)
            
