'''
 Name		: dirstruct.py
 Author		: AdityaM
 Date		: September 8, 2013
'''

import sys
import os

class FileStruct:
	
	def __init__(self, file_path):
		if os.path.isdir(file_path):
			print 'This is not a file and may be a directory'
			print 'Something might be wrong with the directory base'
			print 'case, where the call to create the FileStruct is'
			print 'being made'
		self.file_name = file_path
		with open('test.txt', 'a') as test:
			test.write('%s\n'%self.file_name)

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
		self.parent = dir_path

		#Check if the path entered is a directory
		self.is_dir = os.path.isdir(self.parent)
		with open('test.txt', 'a') as test:
			test.write('%s\n'%self.parent)
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
		all_files = os.listdir(self.parent)
		self.number_of_files = len(all_files)
		for each in all_files:
			print each
			child_path = os.path.join(self.parent,each )
			if os.path.isdir(child_path):
				'''
				If the child is a directory instantiate and add to the
				list of children
				'''
				self.children.append(DirStruct(child_path))
			else:
				'''
				This here is the base case that deals with the files,
				and not the directories.
				I could give the names the same named variable in both
				the File and the directory struct to make printing easier,
				but it might be better to leave both differet so as to facilitate
				debugging.
				'''
				self.children.append(FileStruct(child_path)	)

