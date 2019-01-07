import sys, os, errno
import re
import xlsxwriter
import pandas as pd
import numpy as np
from nltk.tokenize import WhitespaceTokenizer
from pandas import ExcelWriter
from pandas import ExcelFile


def clear(): return os.system('clear')


fh = open('testfile.txt', 'w')

file = 'demo.xlsx'
exportfile = 'export_result.xlsx'

xl = pd.ExcelFile(file)
df = pd.read_excel(file, sheet_name='Sheet1')


# Create a `CheckWord` class
class CheckWord(object):
    def finder(self, string):
        # text = re.sub(r' ', "", string)
        text1 = re.sub(r"(?:\()([^\()\)]+)(?:\))","", string)
        text2 = re.sub(r"([\®]([\W\d.-]+))","", text1)
        result_list = re.sub(r"(?:\()([^\()\)]+)(?:\))","", text2)
        result_list1 = re.sub(r"(?:\[)([^\()\)]+)(?:\])","", result_list)
        result_list2 = re.sub(r'[,]|[.]|[๐-๙]', "", result_list1)
        return result_list2

    def remove_duplicates(self, string):
        output = []
        seen = set()
        for value in string:
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output

    def append_word(self, string):
        output = []
        semicolon_value = []
        for value in string:
            # output.append(value)
            if value.endswith(';') :
                semicolon_value.append(value)
            else : 
                output.append(value)
        return output

text = CheckWord()

english = []
thai = []
thai_result_list = []
english_result_list = []
clear()
for i in df.index:
    english.append(df['EN_INPUT'][i])
    thai.append(df['TH_INPUT'][i])
    textList = df['EN_INPUT'][i]
    # /print(df['EN_INPUT'][i], ' | ', df['TH_INPUT'][i])
    if (textList != ' ' ) and (str(textList).lower() != 'nan')  :
        xx = text.finder(textList) 
        if (xx != '' ) and (str(xx).lower() != 'nan') or (str(xx).lower() != '')  :
            # print(i,df['EN_INPUT'][i],' | ',xx)
            english_result_list.append(xx)
            # english_result_list = text.remove_duplicates(xx)
            # print(str(xx))
            # clear()
            # fh.writelines(str(df['EN_INPUT'][i]))

dd = []
dd = text.remove_duplicates(english_result_list)
xx = []
# for row in dd:
#     # print(row.__len__(),row)
    
#     ff = text.append_word(row)
    # xx.append(ff)
    # fh.writelines(str(ff)+'\n')


output = []
semicolon_value = []
for value in dd:
    # output.append(value)
    if value.endswith(';') :
        semicolon_value.append(value)
        # fh.writelines(str(value)+'\n')
    else : 
        output.append(value)
    
        # fh.writelines(str(value)+'\n')
    fh.writelines(str(value)+'\n')

print("Update Success file:", exportfile)
fh.close()
