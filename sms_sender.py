#!/usr/bin/env python

import urllib
import urllib2
number = raw_input("Please Enter The Phone Number:\n")
message = raw_input("Please Enter Your Message:\n")
prov = ''
url2 = 'http://www.torpedogratuito.com/'
url = 'http://torpedogratis.org/'
values2 = {'action' : 'lookup',
           'pre' : number[0:3],
           'ex' : number[3:6],
           'myButton' : 'Find Provider'}
data2 = urllib.urlencode(values2)  ##provider checker
req2 = urllib2.Request(url2, data2)
response2 = urllib2.urlopen(req2)
the_page2 = response2.read()
if 'Telus' in the_page2:
    prov = '192'
if 'Bell' in the_page2:
    prov = '48'
if 'Rogers' in the_page2:
    prov = '162'
if 'Sprint' in the_page2:
    prov = '175'
if 'T-Mobile' in the_page2:
    prov = '182'
if 'Verizon' in the_page2:
    prov = '203'
if 'Virgin Mobile' in the_page2:
    prov = '205'
if 'AT&T' in the_page2:
    prov = '41'
print prov
if prov == 0:
    print "Failed To Identify Provider\n"
    exit
values = {'code' : '',
          'number' : number,
          'from' : '',
          'remember' : 'n',
          'subject' : '',
          'carrier' : prov,
          'quicktext' : '',
          'message' : message,
          's' : 'Send Message'}
data = urllib.urlencode(values)  ##text sender
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read() 
