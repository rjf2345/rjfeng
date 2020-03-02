
from selenium import webdriver
import time
import schedule
from selenium.webdriver.support.select import Select

def log_in(drive):    
    drive.get('http://jksb.zzu.edu.cn/')
    drive.refresh()
    drive.switch_to_frame("my_toprr")
    user_box = drive.find_element_by_name('uid')
    user_box.send_keys('201677H0730')
    #passwd_box = drive.find_element_by_name('upw')
    #passwd_box.send_keys('0520351X')
    load_box = drive.find_element_by_name('smbtn')
    load_box.click()

def submitpage1(drive):
    current_window = drive.current_window_handle
    drive.switch_to_frame("zzj_top_6s")
    submit1 = drive.find_element_by_xpath('//div[@onclick="myform52.submit()"]')
    submit1.click()
    time.sleep(1)
    current_window = drive.current_window_handle
    select = Select(drive.find_element_by_name("myvsp_5"))
    select.select_by_value("正常")

    submit2 = drive.find_element_by_xpath('//div[@onclick="myform52.submit()"]')
    submit2.click()
    print("打卡成功")
def start():
    drive = webdriver.Edge()
    log_in(drive)
    time.sleep(2)
    submitpage1(drive)
    


schedule.every().day.at("09:00").do(start)
while True:
    schedule.run_pending()
    time.sleep(1)
