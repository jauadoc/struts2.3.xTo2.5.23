#!/usr/bin/python -O
# coding: UTF-8
"""
-
v0.1
-------------------------------------------------------------------------------
usage:
    FileSearch.xx
-------------------------------------------------------------------------------
"""
__author__ = "javadoc"
__version__ = "0.1"

import os
import re


class FileSearch:

    def __init__(self):
        pass

    # Search name match file_name_reg files in path
    @staticmethod
    def search_file(path, file_name_reg):
        file_list = [];

        cur_dir_files = os.listdir(path)
        for file_path in cur_dir_files:
            try:
                path_temp = os.path.join(path, file_path)
                if os.path.isdir(path_temp):
                    temp_list = FileSearch.search_file(path_temp, file_name_reg);
                    if len(temp_list) > 0:
                        for tempJsp in temp_list:
                            file_list.append(tempJsp);
                elif re.search(file_name_reg, file_path):
                    file_list.append(path_temp)
            except Exception,e:
                print("Oops, this path open occur exception, please try again" + path_temp)
                print 'str(Exception):\t', str(Exception)
                print 'str(e):\t\t', str(e)
        return file_list;

    # get current py file path directory
    @staticmethod
    def get_cur_py_path():
        pwd = os.getcwd()
        return pwd;