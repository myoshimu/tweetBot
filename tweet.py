#!/usr/bin/env/python
#-*- coding: utf-8 -*-

import urllib,urllib2
import simplejson
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import BeautifulSoup

url = 'https://www.google.co.jp/alerts/feeds/13699247032203090619/14874934891899781372'
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
values={}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
page = response.read()

soup = BeautifulStoneSoup(page)(formatter=None)
title=str(soup.entry.title)[18:-8]

link=str(soup.entry.link)[12:-9]


API_URL = 'https://www.googleapis.com/urlshortener/v1/url'
API_KEY = None

def shorten(longUrl):
    if isinstance(longUrl, unicode):
        longUrl = longUrl.encode('utf-8')
       
    if API_KEY is None:
        data = '{longUrl:"%s"}' % (longUrl)
    else:
        data = '{longUrl:"%s", key:"%s"}' % (longUrl, API_KEY)
    req2 = urllib2.Request(API_URL, data)
    req2.add_header('Content-Type', 'application/json')
    
    result = urllib2.urlopen(req2)
    return simplejson.loads(result.read()).get('id')

print shorten(link)