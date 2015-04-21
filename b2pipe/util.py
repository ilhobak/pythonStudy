# -*- coding: utf-8 -*-
# util

import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_user_name():
    curUserName = os.getenv('USERNAME')
    return curUserName

def get_folder_list(path):
    for root, dirs, files in os.walk(path):
        return dirs

def b2HistoryParsing(file , filter = 'all'):

    f = open(file, 'r')
    s = f.read()
    data = unicode(s, 'euc-kr').encode('utf-8') 

    notes = data.split("</note>")
    # print notes[0]
    # comment = re.search('<comment>(.+)</comment>',notes[0])
    # print comment.group(1)

    history = []
    tags = ['author', 'date', 'time', 'event', 'version', 'comment']

    notes.reverse()

    for note in notes:

        # remove empty string.
        if note.strip() == "":
            continue

        # print note
        curHistory = []
        for tag in tags:
            # tag로 정규식 검색,  comment는 여러줄이라 re.S compile 사용.
            p = re.compile(('<'+ tag + '>(.+)</' + tag +'>'), re.S)
            result = p.search(note)
            if result == None:
                continue
            else:
                curHistory.append(result.group(1))

        history.append(curHistory)

    return history

def b2HistoryAdd(file):

    text = ("""Author: %s
Date: %s %s
Event: %s (Version: %s)
Comment:
%s
""" % (file[0], file[1], file[2], file[3], file[4], file[5]))

    return text


if __name__ == '__main__':
    # a = get_folder_list("P:\\1302_Chu\\")
    # print a

    a = b2HistoryParsing("P:/1304_D40/4.Asset/cha/asr/mdl/_info/cha_asr_mdl_History.xml" )
    b = b2HistoryAdd(a[1])
    print b


