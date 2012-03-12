#!/usr/bin/env python

#author:Jims of http://www.ringkee.com/
#create date: 2005/02/05
#description: Using ftplib module upload a file to a ftp server.
import os
import zipfile
from ftplib import FTP
import datetime
#
#
#
import os,zipfile,sys
from os.path import join
from datetime import date
backTime=datetime.date.today().isoformat() 
def zipfolder(foldername,filename):
	empty_dirs=[]
	zip=zipfile.ZipFile(filename,'w',zipfile.ZIP_DEFLATED)
	for root,dirs,files in os.walk(foldername):
		empty_dirs.extend([dir for dir in dirs if os.listdir(join(root,dir))==[]])
		for filename in files:
			#print "compressing",join(root,filename)
			#.encode("utf-8")
			zip.write(join(root,filename))
			#.encode("utf-8"))
	for dir in empty_dirs:
		zif=zipfile.ZipInfo(join(root,dir))#.encode("utf-8"+"/"))
		zip.writestr(zif,"")
	zip.close()
	print "Finish compressing"

def usage(number):
	print '''usage:<srcdir> <dstdir> <ftp server address> <ftp port> <user name> <password>'''
	if number<3:
		print ''' <srcdir> <dstdir> is a must'''
		return 0
	if  number<5:
		print ''' default ftp server: 192.168.0.254'''
		print ''' default ftp port 21'''
		print ''' default ftp user anonymous'''
		return 1
	return 2
#
#
#

def upload(ftp_server,port,filename,destName,user,password):
	ftp=FTP()
	ftp.set_debuglevel(2)
	ftp.connect(ftp_server,port)
	ftp.login(user,password)
	print ftp.getwelcome()
	ftp.dir()
	ftp.cwd('incomming/backup/')
	bufsize=4096
	file_handler=open(filename,'rb')
	ftp.storbinary('STOR '+destName,file_handler,bufsize)
	ftp.set_debuglevel(0)
	file_handler.close()
	ftp.quit()
#
#
#
def db_backup(ftp_server,port,user,password):
	db_name='joomla'
	db_user='root'
	db_password='earth'
	dumpdes='joomla_backup.back'+backTime
	temdir='/tmp/'
	shellcmd='mysqldump -u'+db_user+' -p'+db_password+' '+db_name+' >'+temdir+dumpdes
	print shellcmd
	os.system(shellcmd)
	upload(ftp_server,port,temdir+dumpdes,dumpdes,user,password)
	#mysqldump -u[user] -p[password] [databasename] > [dump_name] 

#
#
def all_back_up():
	argv=sys.argv
	argc=len(argv)
	ret=usage(argc)
	temdir='/tmp/'
	ftp_server="192.168.0.254"
	port="21"
	user="ftp"
	password="earth@709"
	if 1==ret:
		srcDir=argv[1]
		filename=argv[2]+backTime
		zipfolder(srcDir,temdir+filename)
		upload(ftp_server,port,temdir+filename,filename,user,password)
		db_backup(ftp_server,port,user,password)
	elif 2==ret:
		if argc>=4:
			ftp_server=argv[3]

		if argv>=5 :
			port=argv[4]
		if argc>=6:
			user=argv[5]
		if argc>=7:
			password=argv[6]
	
		srcDir=argv[1]
		filename=argv[2]+time.time()
		zipfolder(srcDir,temdir+filename)
		upload(ftp_server,port,temdir+filename,filename,user,password)
		db_backup(ftp_server,port,user,password)

		
		

all_back_up()
