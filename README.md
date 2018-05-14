```
				 _      _____  _    _           _ _      
                | |    / __  \| |  (_)         | | |     
 _ __  _   _ ___| |__  `' / /'| | ___ _ __   __| | | ___ 
| '_ \| | | / __| '_ \   / /  | |/ / | '_ \ / _` | |/ _ \
| |_) | |_| \__ \ | | |./ /___|   <| | | | | (_| | |  __/
| .__/ \__,_|___/_| |_|\_____/|_|\_\_|_| |_|\__,_|_|\___|
| |                                                      
|_|                                                      
```
                                                                        
# INTRODUCTION 
push2kindle is designed to  push documents (.txt, .doc, .pdf, etc) to designated kindle. 
push2kindle is supported in all common platforms (windows, linux, macos).



# PREREQUISITES

* python (python 2 and python 3 are both supported)  
It was installed by default for most Linux distribution and MAC.  
If not, please check [https://www.python.org/downloads/](https://www.python.org/downloads/) for installation 
instructions. 

# INSTALLATION
  
* __Option 1: Install from download directory__   
	cd to the downloaded  package root directory

	run python setup to install   

	```shell
	$python setup.py install
	```
		
	MacOS or Linux users might need the sudo/root access to install. 
	Users without the root access can install the package using the pip/easy_install with a --user parameter ([install python libraries without root](https://stackoverflow.com/questions/7465445/how-to-install-python-modules-without-root-access))．
	 
	```shell  
	$sudo python setup.py install 
	```
	use python3 instead of python in the above commands to install if using python3. 
	
* __Option 2: Install from Github__:    

	python 2:  
	```shell
	$sudo pip install --upgrade https://github.com/phoenixding/push2kindle/zipball/master
	```
	python 3: 
	```shell
	$sudo pip3 install --upgrade https://github.com/phoenixding/push2kindle/zipball/master
	```
 
# USAGE

```
push2kindle <file 1> <file 2> ...<file n>
```

Note: this is a 50MB limit by Amazon.

The users might need to setup a config file at the first run. 
The config file path will be given by the program.


__config format: (tab-delimited)__  

fromaddr	your@email.com  
toaddr	yourkindle@kindle.com  
user	username_for_fromaddr_email  
password	password_for_fromaddr_email  
smtp	smftp_server(if google, you can use sftp.google.com:587)  

Note: please add your fromaddr email account into the "Approved Personal Document E-mail List" in your amazon kindle setting.
                   
# CREDITS
 
This software was developed by Jun Ding


# LICENSE 
 
This software is under MIT license.  
see the LICENSE.txt file for details. 


# CONTACT

jund  at cs.cmu.edu




                                 
                                 
                                 
                                 
                                 

                                                     
