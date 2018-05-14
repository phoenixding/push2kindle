from setuptools import setup
import sys

setup(  name='push2kindleUniversal',
		version='1.0',
		description='push2kindle in all platforms',
		author='Jun Ding',
		author_email='jund@cs.cmu.edu',
		license='MIT',
		packages={'push2kindle'},
		data_files=[(sys.prefix+'/push2kindle_config/',['config/config.txt'])],
		entry_points={'console_scripts':['push2kindle=push2kindle.push2kindle:main']},
		classifiers=[
			'Development Status :: 3 - Alpha',
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 2',
			'Programming Language :: Python :: 3',
		],
		)
