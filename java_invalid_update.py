#!/usr/bin/python -O
# coding: UTF-8
"""
-struts2.3.x to struts2.5.23
--replace invalid usage of tag <s:text>, invalid usage like <s:text name="中文">
-------------------------------------------------------------------------------
"""

__author__ = "javadoc"
__version__ = "0.1"

import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def find_invalid_field(file_name, regex):
    f_read = open(file_name)
    line_num = 0
    matched = False
    try:
        num = 0
        for each_line in f_read:
            line_num += 1
            match = re.findall(regex, each_line)
            if match:
                num += 1
                matched = True
                if num <= 1:
                    print("----start----file [%s]" % file_name)
                for i in xrange(0, len(match)):
                    print("==line:[%d] matched: [%s]" % (line_num, match[i]))
        f_read.close()
    except Exception, e:
        print("Oops, find occur exception, file name is:" + file_name +"; line is:%d" % line_num)
        print("str(Exception):\t[%s]" % str(Exception))
        print('str(e):\t\t[%s]' % str(e))
    if matched:
        print("----e n d----file [%s]" % file_name)
        print("")

    return matched