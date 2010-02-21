#!/usr/bin/env python
#encoding = utf-8
# 
# author: Zhicheng Wei <zhicheng1988@gmail.com>
# Copyright (c) 2009 Zhicheng Wei
#

import urllib2

from BeautifulSoup import BeautifulSoup

page_num = 2
def parsing_page(url):
    print url
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    for embed in soup.findAll('embed'):
        swf_url = dict(embed.attrs)['src']
        print swf_url

def parsing_index_page(url):
    index_page = urllib2.urlopen(url)
    soup = BeautifulSoup(index_page)
    for div_for_page in soup.findAll('div', attrs={'class':'post f'}):
        page_url = dict(div_for_page.h2.a.attrs)['href']
        parsing_page(page_url)

    global page_num
    next_page_url = 'http://jandan.net/category/playbus/page/%d' % page_num 
    page_num += 1
    print next_page_url
    parsing_index_page(next_page_url)
    if page_num > 19: return

if __name__ == '__main__':
    start_url = "http://jandan.net/category/playbus/"
    parsing_index_page(start_url)

