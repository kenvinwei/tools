#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
import sys
import zipfile

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: gbkzip < zipfile.zip >'
        exit(1)

    try:
        zip_obj = zipfile.ZipFile(sys.argv[1], 'r')
    except IOError as e:
        print e.strerror
        exit(1)

    for name in zip_obj.namelist():
        name_utf8 = name.decode('gb2312')
        path = os.path.dirname(name_utf8)

        if (not os.path.exists(path)) and path:
            os.makedirs(path)
        #Start Exacting
        filedata = zip_obj.read(name)
        if not os.path.exists(name_utf8):
            tmp = open(name_utf8, 'w')
            tmp.write(filedata)
            tmp.close()
        print 'Exacting %s ... done!'% (name_utf8)
    zip_obj.close() 
