# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 11:30:57 2015

@author: kenneddp
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

import time, urllib2
from HTMLParsers import DataCollector

url = 'https://rdcrnqa.epi.usf.edu//rdnwebapp/Forms/05VCRC/5532/RecurringMedications.aspx?EventScheduleId=12658&RdcrnProtocolId=5532&ProtocolId=363&creguid=1697&trimester=4'
page = urllib2.urlopen(url)
html = page.read()

driver = webdriver.Firefox()
driver.get(url)            
time.sleep(5)


checkbox_info = DataCollector(html)

for id, value in checkbox_info:
    if "no medications" in value.lower():
        pass
    else:
        driver.find_element_by_id(id).click()

print 'Complete'


