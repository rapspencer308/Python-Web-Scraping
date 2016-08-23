import urllib2
import simplejson
from BeautifulSoup import BeautifulSoup
import requests
import sys
import time
import re



start_time = time.time()
print start_time
print

def p():#Debugging function
    line = str(sys.exc_traceback.tb_lineno)
    print "----------------------------------------Error at: " + line

def getNamesListInDivs():#Gets list item from website, but list is across 5 pages on site, for each list item it adds it to html list
    x = 1
    while x <= 5:#going though 5 pages. Loops this 5 times
        try:#it will try the script below

            url = "http://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"+str(x)
            a = requests.get(url)
            soup = BeautifulSoup(a.content)
            container = soup.findAll("tbody")#there is only 1 tbody so I dont have to be specify the tag's attribute value like a class name.

            for shit in container:#for each of the table rows in the table body

                thumbs = shit.findAll("td", {"class": "name"})#find the element with the Billionaire's name

                for shit2 in thumbs:#for shit in the element

                    print "<div>" + shit2.text + "</div>"#print the text of the element

        except:#if there was and error with the script it will call the debugging function.
            p()
            pass#then go on to the next loop
        x = x + 1

def createBookmarks(): #turns html list of names into chrome bookmarks
    url = urllib2.urlopen("file:///C:/Users/CPU/Desktop/pythonWebScraping/namesListInDiv.html").read()  #put your file location in
    soup = BeautifulSoup(url)
    print '''----start----

    <!DOCTYPE NETSCAPE-Bookmark-file-1>
    <!-- This is an automatically generated file.
         It will be read and overwritten.
         DO NOT EDIT! -->
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
    <TITLE>Bookmarks</TITLE>
    <H1>Bookmarks</H1>
    <DL><p>
        <DT><H3 ADD_DATE="1470292583" LAST_MODIFIED="1470292630" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks bar</H3>
        <DL><p>
            <DT><H3 ADD_DATE="1470292630" LAST_MODIFIED="1470292637">New folder</H3>
            <DL><p>
    '''
    g_data = soup.findAll("div")
    x = 1
    for shit in g_data:#for each list item
        name = shit.contents[0]
        name2 = (shit.text).replace(" ", "+")#replace the space in the name to create the link url
        a = "http://www.pornhub.com/video/search?search=" + name2 #http://www.pornhub.com/video/search?search=firstName+lastName
        link = a
        open = '<DT><A HREF="'
        end = '" ADD_DATE="1470292609">' + name + ' - ' + str(x) + '</A>'
        tag = open + link + end
        print tag
        x = x + 1
    print '''        </DL><p>
        </DL><p>
    </DL><p>




    ----end----


    '''

def namesListToGettingData():
    url = urllib2.urlopen("file:///C:/Users/CPU/Desktop/pythonWebScraping/namesListInDiv.html").read()  #put your location to div list in
    soup = BeautifulSoup(url)
    g_data = soup.findAll("div")
    for shit in g_data:
        try:
            name = shit.contents[0]
            name2 = (shit.text).replace(" ", "+")
            a = "http://www.therichest.com/search/" + name2  # https://en.wikipedia.org/wiki/Bill_Gates
            #print a
            url2 = requests.get(a)
            soup2 = BeautifulSoup(url2.content)
            table = soup2.findAll("div", {"class": "search-list"})
            for rows in table:
                x = 1
                while x <= 1:
                    imgBase = rows.findAll("div", {"class": "responsiveImg img_search_page"})[0]["data-src-base"]
                    imgAdd = rows.findAll("div", {"class": "responsiveImg img_search_page"})[0]["data-image"]
                    img = imgBase + imgAdd
                    headline = rows.findAll("h2", {"class": "title"})[0].text
                    excerpt = rows.findAll("div", {"class": "excerpt"})[0].text

                    print img + " --- " + headline
                    x = x + 1
        except:
            pass


#Functions: uncomment one and run one at a time.

getNamesListInDivs()
#createBookmarks()
#namesListToGettingData()


print
print "My program took", time.time() - start_time, "seconds to run"