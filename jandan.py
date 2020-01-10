import urllib2
from bs4 import BeautifulSoup
#要抓取的链接
url="http://jandan.net"
#获取新闻列表
def getNewsList():
    request=urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
    html = urllib2.urlopen(request)
    soup = BeautifulSoup(html, "html.parser")
    print """<!DOCTYPE html>
    <html lang="en">
    <head><meta charset="UTF-8"></head>
    <body>"""
    #循环打印新闻链接和新闻标题
    for h2 in soup.find_all("h2"):
        link=h2.find_all("a")[0].get("href")
        title=h2.get_text()
        print '         <a href="',link,'">',title,'</a>'
        print "         <br>"
    print """   </body>
</html>"""
getNewsList()
