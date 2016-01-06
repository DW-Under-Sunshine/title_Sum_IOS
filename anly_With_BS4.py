from bs4 import BeautifulSoup
import open_html
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def find_Link(html):

    soup = BeautifulSoup(html)
    # if soup['class'] == "lesson-info-h2":
    #     print 1
    content = soup.find_all('h2')
    print 1
    for each_Line in content:
        print each_Line.string
        f1.writelines(str(each_Line.string)+'\n')



f1 = open('Sum_IOSClass_JK.txt','w+')
for i in range(1,7):
    html_link = 'http://www.jikexueyuan.com/course/ios/?pageNum='+str(i)
    # print html_link
    html = open_html.web_content(html_link)
    find_Link(html)
    # print 1
f1.close()