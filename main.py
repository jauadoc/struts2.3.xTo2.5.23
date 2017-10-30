#!/usr/bin/python -O
# coding: UTF-8
"""
-struts2.3.x to struts2.5.23
-- replace or find some invalid usage in before version of jsp/java file
v1.0
-------------------------------------------------------------------------------
usage:
    put this file in your project root path
    python xx.py > /your_path/result.txt
-------------------------------------------------------------------------------
"""

__author__ = "javadoc"
__version__ = "0.1"


from java_invalid_update import find_invalid_field
from struts_tag_update import *

from FileOpr import FileSearch

FileSearch()


# replace invalid usage of tag <s:text>, invalid usage like <s:text name="中文">
def replace_invalid_struts_text_tag():
    print("****************replace invalid usage of <s:text> start...****************");
    scan_path = FileSearch.get_cur_py_path();
    jsp_file_list = FileSearch.search_file(scan_path, ".*?\.jsp$");

    print("====scan path is [%s]" % scan_path);
    print("====find jsp count:[%d]" % (len(jsp_file_list)));
    print("======================changed log start...======================");
    changed_jsp_list = []
    for jspFile in jsp_file_list:
        replace_flag = text_repair(jspFile);
        if replace_flag:
            changed_jsp_list.append(jspFile)
    print("======================changed log end============================");

    print("======================replace file log start...==================");

    print("====replace jsp count[%d]" % (len(changed_jsp_list)));
    i = 1;
    for file_name in changed_jsp_list:
        print("file[%d]:%s" % (i, file_name));
        i += 1;

    print("======================replace file log end========================");
    print("****************replace invalid usage of <s:text> end****************");
    print("\n\n\n")


# replace struts some tag filed id to var;
# which tag in[action,append,bean,date,generator,iterator,merge,number,set,sort,subset,text,url]
def replace_struts_tag_id2var():
    print("****************replace id to var of <s:text> start...****************");
    scan_path = FileSearch.get_cur_py_path();
    jsp_file_list = FileSearch.search_file(scan_path, ".*?\.jsp$");

    print("====scan path is [%s]" % scan_path);
    print("====find jsp count:[%d]" % (len(jsp_file_list)));
    print("======================changed log start...======================");
    changed_jsp_list = []
    for jspFile in jsp_file_list:
        replace_flag = id2var(jspFile);
        if replace_flag:
            changed_jsp_list.append(jspFile)
    print("======================changed log end============================");

    print("======================replace file log start...==================");
    print("====replace jsp count[%d]" % (len(changed_jsp_list)));
    i = 1;
    for file_name in changed_jsp_list:
        print("file[%d]:%s" % (i, file_name));
        i += 1;

    print("======================replace file log end========================");
    print("****************replace id to var of <s:text> end****************");
    print("\n\n\n")


# find error field in java file, like [private String sText;], it make struts can't set value into field
def find_error_field_with_getset():

    print("****************find invalid java field name start...****************");
    scan_path = FileSearch.get_cur_py_path()
    matched_file_list = FileSearch.search_file(scan_path, ".*?(_Action|_Form)\.java$");

    print("====scan path is [%s]" % scan_path);
    print("====find file count:[%d]" % (len(matched_file_list)));
    print("======================matched log start...======================");
    for matchedFile in matched_file_list:
        find_invalid_field(matchedFile, "(private\s+?[a-zA-Z]+?\s+?[a-z]{1}[A-Z]{1}[a-zA-Z]+?;)");
    print("======================matched log end===========================");
    print("****************find invalid java field name end****************");
    print("\n\n\n")


def main():
    replace_invalid_struts_text_tag()
    replace_struts_tag_id2var()
    find_error_field_with_getset()
    pass


if __name__ == "__main__":
    main();