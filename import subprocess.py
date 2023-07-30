import subprocess
from time import sleep
from clicknium import clicknium as cc, locator, ui
from clicknium.common.enums import ClearHotKey,PreAction,InputTextBy,MouseButton,MouseActionBy,Location
from clicknium.common.models.mouselocation import MouseLocation

exePath="F:/Scoop/apps/tim/current/Bin/QQScLauncher.exe"
accounts = {}
def readfile():
    with open('F:/code/source/auto/data/accounts.txt', 'r') as f:   
      for line in f:
          username, password = line.strip().split(':')
          accounts[username] = password



# 启动进程
def start_process():
    path = exePath
    subprocess.Popen(path)  # 通过 subprocess 库来启动tim进程
    sleep(3)
    print('start_process end.')

def login(account,pas):
    username=account
    password=pas
    ui(locator.tim.qq).clear_text('send-hotkey',ClearHotKey.CtrlA_Delete,PreAction.Click)    
    cc.send_text(username)
    cc.send_hotkey('{enter}')
    ui(locator.tim.pas).click()
    cc.send_text(password)
    cc.send_hotkey('{enter}')
    ui(locator.tim.login).click()


def main():
    # if cc.chrome.extension.install_or_update():
    #   print("Please open edge browser to enable clicknium extension, then run sample again.")
    #   return
    # sample code to demo web automation and desktop application
    #tab = cc.chrome.open("https://www.bing.com/")
    # tab.find_element(
    #     locator.sample.bing.search_sb_form_q).set_text('clicknium')
    # tab.find_element(locator.sample.bing.svg).click()
    # sleep(3)
    # tab.close()
    # process = subprocess.Popen("notepad")
    # ui(locator.sample.notepad.document_15).set_text("clicknium")
    readfile()
    for account in accounts:
      start_process()
      login(account,accounts[account]) 
      sleep(5)
      
    sleep(85) 

if __name__ == "__main__":
    main()



