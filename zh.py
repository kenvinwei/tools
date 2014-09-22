#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author kenvinwei
# @date 2014/09/22
# python v3.4.1
import sys
def run():
	mlist = sys.argv;
	if(sys.argv[1]):
		mystr = sys.argv[1]
		if(mystr.startswith('\\u')):
			print(mystr.encode().decode('unicode-escape'))
		else:
			print("error data")
	else:
		print('can not get argv[1]');

if __name__=="__main__":
	run();


