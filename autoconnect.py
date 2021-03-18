from pywinauto import application
import time
import os
import configparser

from configparser import ConfigParser

parser = ConfigParser()
parser.read('config')

#print(parser.sections())  
id = parser.get('account', 'id')
pwd = parser.get('account', 'pwd')
pwdcert = parser.get('account', 'pwdcert') 


os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)        

appStart='C:\CREON\STARTER\coStarter.exe /prj:cp /id:'+id+' /pwd:'+pwd+' /pwdcert:'+pwdcert+' /autostart'

app = application.Application()
app.start(appStart)
time.sleep(60)