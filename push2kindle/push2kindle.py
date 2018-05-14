#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author: jun ding
date: May 10th, 2018
usage: push2kindle <file 1> <file 2> ...<file n>
Note: this is a 50MB limit by Amazon.

config format: (tab-delimited)
fromaddr	your@email.com
toaddr	yourkindle@kindle.com
user	username_for_fromaddr_email
password	password_for_fromaddr_email
smtp	smftp_server(if google, you can use sftp.google.com:587)

Note: please add your fromaddr email account into the "Approved Personal Document E-mail List" in your amazon kindle setting.
"""

import pdb,sys,os
import smtplib
from email import encoders


if int(sys.version[0])<3:
    reload(sys)
    sys.setdefaultencoding('utf8')
    from email.MIMEBase import MIMEBase
    from email.MIMEMultipart import MIMEMultipart
else:
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
import pkg_resources
configfile=sys.prefix+'/push2kindle_config/config.txt'
print(configfile)

def main():
	# read in config
	#pdb.set_trace()
	
	try:
		with open(configfile,'r') as f:
			configs=f.readlines()
			configs=[item.strip().split() for item in configs]
			dconfig={}
			for i in configs:
				dconfig[i[0]]=i[1]
		
		fromaddr=dconfig['fromaddr']
		toaddr=dconfig['toaddr']
		user=dconfig['user']
		password=dconfig['password']
		smtp=dconfig['smtp']
		print(dconfig)
	except:
		
		print("please check the format of your config.txt file")
		print("if it's your first run, plese modify the config file accordingly")
		print("the config file is located at :%s" %(configfile))
		print("-------")
		print(__doc__)
		sys.exit(0)

	#=============================================		
	# add the attachment
	# attachment file
	attachments=sys.argv[1:]
	if len(attachments)<1:
		print('check your inputs')
		print(__doc__)
		sys.exit(0)
	
	try:
		#pdb.set_trace()
		msg = MIMEMultipart()
		msg['Subject']='convert'
		for file in attachments:
			fp = open(file, 'rb')
			part = MIMEBase('application', "octet-stream")
			part.set_payload((fp).read())
			encoders.encode_base64(part)
			fp.close()
			part.add_header('Content-Transfer-Encoding', 'base64')
			part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
			msg.attach(part)   # msg is an instance of MIMEMultipart()

		print('sending document ...')
		# send the attachment via email
		smtp=smtplib.SMTP(smtp)
		smtp.ehlo()
		smtp.starttls()
		smtp.login(user,password)
		smtp.sendmail(fromaddr,toaddr,msg.as_string())
		smtp.quit()
		print('done! please sync your kindle')
	except:
		print("error, please check your input for config file: %s"%(configfile))
		print(__doc__)
		

if __name__=="__main__":
	main()
