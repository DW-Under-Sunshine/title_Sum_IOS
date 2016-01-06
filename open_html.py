import urllib
import urllib2

def web_content(web_link):
    link_use = web_link
    # body = ''
    # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    # headers = { 'User-Agent' : user_agent }
    # request = urllib2.Request(link_use,body,headers)
    response = urllib2.urlopen(link_use)
    html =response.read()
    return html