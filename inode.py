# InodePy
import os,sys
import time
import stat
import datetime
from stat import *
class inode:
	def print_details(self,a):
		print "\nInode information"
		print "Device:",os.stat(a).st_dev
		print "Inode:",os.stat(a).st_ino
		print "Mode",os.stat(a).st_mode
		print "Size:",os.stat(a).st_size
		print "Links:",os.stat(a).st_nlink
		print "Uid:",os.stat(a).st_uid
		print "Gid:",os.stat(a).st_gid
		print "Last modified Time",datetime.datetime.fromtimestamp(int(os.stat(a).st_mtime))
		print "Last status change Time",datetime.datetime.fromtimestamp(int(os.stat(a).st_ctime))
		print "Last accessed Time",datetime.datetime.fromtimestamp(int(os.stat(a).st_atime))
		#print time.ctime(os.stat(a)[9])
		#print time.asctime(time.localtime(os.stat[a]))
		#print time.mtime(os.stat(a)[9])

	def perm(self,a):
		mode = os.stat(a).st_mode
		ur = bool(mode & stat.S_IRUSR)
		uw = bool(mode & stat.S_IWUSR)
		ux = bool(mode & stat.S_IXUSR)
		gr = bool(mode & stat.S_IRGRP)
		gw = bool(mode & stat.S_IWGRP)
		gx = bool(mode & stat.S_IXGRP)
		oor = bool(mode & stat.S_IROTH)
		ow = bool(mode & stat.S_IWOTH)
		ox = bool(mode & stat.S_IXOTH)
		if ur:
			sys.stdout.write('r')
		else:
			sys.stdout.write('-')
		if uw:
			sys.stdout.write('w')
		else:
			sys.stdout.write('-')
		if ux:
			sys.stdout.write('x')
		else:
			sys.stdout.write('-')
		if gr:
			sys.stdout.write('r')
		else:
			sys.stdout.write('-')
		if gw:
			sys.stdout.write('w')
		else:
			sys.stdout.write('-')
		if gx:
			sys.stdout.write('x')
		else:
			sys.stdout.write('-')
		if oor:
			sys.stdout.write('r')
		else:
			sys.stdout.write('-')
		if ow:
			sys.stdout.write('w')
		else:
			sys.stdout.write('-')
		if ox:
			print ('x')
		else:
			print ('-')

	def type(self,a):
		mode = os.stat(a).st_mode
		if S_ISREG(mode):
			print 'Regular File'
			fileopen=open(a,"a")
			b=raw_input("Enter data into File\n")
			fileopen.write(b)
			fileopen.close()
		if S_ISDIR(mode):
			print 'Directory'
		if S_ISLNK(mode):
			print 'symbolic link'
		if S_ISBLK(mode):
			print 'block device'
		if S_ISSOCK(mode):
			print 'socket'
		if S_ISCHR(mode):
			print 'character File'		
		
	def prints(self,a):
		fileopen=open(a,"a")
		b=raw_input("Enter data into File\n")
		fileopen.write(b)
		fileopen.close()	

		
a=raw_input("Enter the file path:\n")
ino1=inode()
ino1.print_details(a)
ino1.perm(a)
ino1.type(a)
#ino1.prints(a)
ino1.print_details(a)
ino1.perm(a)
