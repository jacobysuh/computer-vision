import os
import string
import pipes

font = '/Library/Fonts/Courier\ New\ Bold.ttf'

def make_labels(s):
    l = string.printable
    for word in l:
        if word == ' ':
            os.system('convert -fill black -background white -bordercolor white -font %s -pointsize %d label:"\ " 32_%d.png'%(font,s,(s-12)/2))
        if word == '@':
            os.system('convert -fill black -background white -bordercolor white -font %s -pointsize %d label:"\@" 64_%d.png'%(font,s,(s-12)/2))
        elif word == '\\':
            os.system('convert -fill black -background white -bordercolor white -font %s -pointsize %d label:"\\\\\\\\" 92_%d.png'%(font,s,(s-12)/2))
        elif ord(word) in [9,10,11,12,13,14]:
            pass
        else:
            os.system("convert -fill black -background white -bordercolor white -font %s -pointsize %d label:%s \"%d_%d.png\""%(font,s,pipes.quote(word), ord(word),(s-12)/2))

# 12,24,36,48,60,72,84,96
# s/12-1

for i in [12,14,16,18,20,22,24,26]:
    make_labels(i)

