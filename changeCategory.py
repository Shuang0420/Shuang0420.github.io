# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

files = os.listdir(os.getcwd()+'/_posts')
for name in files:
    name = '_posts/' + name
    if not name.endswith('.md'):
        continue
    f = open(name, 'r')
    l = f.readlines(10)
    sub = ''
    subindex = ''
    for index, str in enumerate(l):
        # if str.startswith('categories: Search Engines'):#and str.endswith(']\n'):
        if str.startswith('categories: [Other'):#and str.endswith(']\n'):
            print str
            # sub = 'categories: [NLP,Search Engines] \n'
            sub = 'categories: [Others] \n'
            subindex=index
            break
    if subindex:
        lines = open(name, 'r').readlines()
        fw = open(name,'w')
        lines[subindex]=sub
        fw.write(''.join(lines))
        fw.close()
