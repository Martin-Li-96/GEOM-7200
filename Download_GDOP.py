import selenium.webdriver.common.devtools.v113.database
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import time as t
import re


delay=3
#Proxy IP
proxy="103.130.112.253:5678"

url1="https://www.gnssplanning.com/#/settings"
url2="https://www.gnssplanning.com/#/charts"


driver=webdriver.Chrome()
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s'%proxy)

driver.get(url1)

driver.find_element(By.ID,"inputLatitude").clear()
driver.find_element(By.ID,"inputLatitude").send_keys("S 27° 29' 56.6876\"")
driver.find_element(By.ID,"inputLongitude").clear()
driver.find_element(By.ID,"inputLongitude").send_keys("E 153° 0' 47.4104\"")
driver.find_element(By.ID,"inputHeight").clear()
driver.find_element(By.ID,"inputHeight").send_keys("24")
driver.find_element(By.ID,"inputShadow").clear()
driver.find_element(By.ID,"inputShadow").send_keys("10")


while(1):
    time = driver.execute_script("return document.getElementById(\"inputDay\").value")
    time_zone = driver.execute_script("return document.querySelector(\"#inputTimezone\").value")
    if (time=="2023-08-03"):
        if(time_zone=="number:119"):
            break

    print("!!!")
print("OK!")

driver.execute_script("document.getElementsByClassName(\"col-sm-11\")[0].getElementsByTagName(\"button\")[0].click()")
driver.get(url2)
# WebDriverWait(driver,10,0.5).until(EC.alert_is_present())
pars = "<svg.*>.*</svg>"
while(1):
    innerHTML = driver.execute_script("return document.body.innerHTML")
    svgs=re.findall(pars,innerHTML)
    if(svgs!=[]):
        break
ylabel=re.findall("<g class=\"highcharts-axis-labels highcharts-yaxis-labels\" data-z-index=\"7\">.*?</g>",innerHTML)[2]
ylabel=re.findall(">(\d|\d\.\d)<",ylabel)
ylabel=[float(i) for i in ylabel]

ygride=re.findall("<g class=\"highcharts-grid highcharts-yaxis-grid\" data-z-index=\"1\">.*?</g>",innerHTML)[2]
ygride=re.findall("(\d{0,3}\.\d) L",ygride)
ygride=[float(i) for i in ygride]
interval=(max(ylabel)-min(ylabel))/(max(ygride)-min(ygride))
translate=47

def cal_value(y):
    return (round(((max(ygride)-y-47)*interval)*100))/100


data=re.findall("<g class=\"highcharts-series-group\" data-z-index=\"3\">.*?</path>",svgs[2])
data=re.findall("M.*class",data[0])
data=re.sub("(M|class|\")","",data[0])
data=data.split("L")
data=[i.split()  for i in data]
data=np.array(data)
data=data.astype("float")
value=[cal_value(i) for i in data[:,1]]

dataset=pd.DataFrame({"time":pd.date_range("2023-08-02",periods=len(value),freq="10min"),
                      "GDOP":value})

dataset.to_csv("2023-08-02_GDOP.csv")

