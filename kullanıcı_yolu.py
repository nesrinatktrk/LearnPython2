import os

#print(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))

#dosya yolunu ismini yazarak bulma
#import os
pythonfile = 'merhaba.txt'

# if the file is present in current directory,
# then no need to specify the whole location
print("Path of the file..", os.path.abspath(pythonfile))

#for root, dirs, files in os.walk(r'E:\geeksforgeeks\path_of_given_file'):
#	for name in files:
		
		# As we need to get the provided python file,
		# comparing here like this
#		if name == pythonfile:
#			print(os.path.abspath(os.path.join(root, name)))