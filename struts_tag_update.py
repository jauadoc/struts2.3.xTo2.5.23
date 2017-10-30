#!/usr/bin/python -O
# coding: UTF-8
"""
-struts2.3.x to struts2.5.23
-- 1.replace invalid usage of tag <s:text>, invalid usage like <s:text name="中文">
-- 2.replace struts some tag filed id to var;
---- which tag in[action,append,bean,date,generator,iterator,merge,number,set,sort,subset,text,url]
-------------------------------------------------------------------------------
"""

__author__ = "javadoc"
__version__ = "0.1"

import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# replace jsp file some struts tag id field to var;
# which tag in[action,append,bean,date,generator,iterator,merge,number,set,sort,subset,text,url]
# like <s:text id="abc"/> to <s:text var="abc"/>
def id2var(file_name):
    f_read = open(file_name)
    content = []
    changed = False
    write_flag = False
    pre_deal_flag = "QAZWSXEDCQSCESZASDWSX"
    line_num = 1
    try:
        num = 0
        for each_line in f_read:
            line_num += 1
            regex = "(<s:(action |append |bean |date |generator |iterator |merge |number |set |sort |subset |text |url ){1}[^>]*?id\s*?=\s*?.*?>)"
            match = re.findall(regex, each_line, re.I)
            if match:
                if num <= 0:
                    print("----start----file name is [%s]" % file_name)
                num += 1
                for i in xrange(0, len(match)):
                    # full tag content
                    pre_deal_tag = match[i][0]
                    # replace pre_deal_tag as pre_deal_flag
                    each_line = each_line.replace(pre_deal_tag, pre_deal_flag)

                    # replace id to var temp tag content
                    regex_id = "(<s:" + match[i][1] + "[^>]*?)id(\s*?=\s*?[\"|'].*?>)"
                    matched_id = re.match(regex_id, pre_deal_tag)
                    if matched_id:
                        result = matched_id.group(1) + "var" + matched_id.group(2)
                        print("==[%d] origin: %s" % (num, pre_deal_tag.replace("\t\n", "")))
                        print("==[%d] change: %s" % (num, result))
                        each_line = each_line.replace(pre_deal_flag, result)
                        changed = True
                content.append(each_line)
            else:
                content.append(each_line)
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()
        if changed:
            write_flag = True
        f_read.close()
    except Exception, e:
        print("Oops, replace occur exception, file name is:" + file_name +"; line is:%d" % line_num)
        print("str(Exception):\t[%s]" % str(Exception))
        print('str(e):\t\t[%s]' % str(e))
    if changed:
        print("----e n d----file name is [%s]" % file_name)
        print("")
    return changed and write_flag


# repair invalid usage of <s:text>
# invalid usage like <s:text name="中文">
# make abc<s:text name="中文">abc to abc中文abc
def text_repair(file_name):
    f_read = open(file_name)
    content = []
    changed = False
    write_flag = False
    pre_deal_flag = "QAZWSXEDCQSCESZASDWSX"
    line_num = 0
    try:
        num = 0
        for each_line in f_read:
            line_num += 1
            # 匹配规则必须含有u,可以没有r
            regex = \
                ur"(<s:text name=[\"|']{1}([\u4e00-\u9fa5]+)[\"|']{1}[^>]*?>)"
            pattern = re.compile(regex)
            data_utf8 = each_line.decode('utf8')
            match = pattern.findall(data_utf8)

            if match:
                if num <= 0:
                    print("----start----file name is [%s]" % file_name)
                num += 1
                # print(match)
                for i in xrange(0, len(match)):
                    # full tag content
                    pre_deal_tag = match[i][0]
                    result = match[i][1]
                    # replace pre_deal_tag as pre_deal_flag
                    each_line = each_line.replace(pre_deal_tag, pre_deal_flag)
                    print("==[%d] origin: %s" % (num, pre_deal_tag.replace("\t\n", "")))
                    print("==[%d] change: %s" % (num, result))
                    each_line = each_line.replace(pre_deal_flag, result)
                    changed = True
                content.append(each_line)
            else:
                content.append(each_line)
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()
        if changed:
            write_flag = True
        f_read.close()
    except Exception, e:
        print("Oops, replace occur exception, file name is:[%s]; line is[:%d]" % (file_name,line_num))
        print("str(Exception):\t[%s]" % str(Exception))
        print('str(e):\t\t[%s]' % str(e))
    if changed:
        print("----e n d----file name is [%s]" % file_name)
        print("")
    return changed and write_flag