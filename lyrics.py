# importing modules
import os
import sys
from bs4 import BeautifulSoup as bs
from googlesearch import search
from array import *
import webbrowser as wb
import vlc

# functions


# code
# importing file path name
program_path = sys.argv[1]
#play the song
vlc.MediaPlayer(program_path).play()
# spliting the path with \\ separator
names = program_path.split('\\')

# file name is present after last separator // , but contains '.'
# filename varible holds the actual name of the file
filename = names[len(names) - 1].split('.')[0]

# adding lyrics to the name to make it query

query = filename + " lyrics az"

# doging the google search and saving it to a variable genrator

generator = search(query, tld='com', lang='en', num=10, start=0, stop=10, pause=2.0)

links = ['text']
for x in generator:
    links.insert(len(links), x)

# removing the first test string

links.pop(0)

targetLink = ""
for y in links:
    if y.find("www.azlyrics.com") != -1:
        targetLink = y
    

if targetLink == "":
	print("sorry bro, its my fault")
else:
	wb.open(targetLink, new=2)

input()