from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import *
import time
import schedule
import datetime


def tempCheck():
    driver = webdriver.Chrome("C:\chromedriver.exe")
    # 로그인하기
    driver.get("https://zeus.gist.ac.kr/sys/main/login.do")
    id = driver.find_element_by_id("login_id")
    pw = driver.find_element_by_id("login_pw")

    id.send_keys(userid)
    pw.send_keys(userpw)
    pw.send_keys(Keys.ENTER)

    driver.implicitly_wait(15) #로그인 이후 로딩을 기다려준다.

    # 건강검진자가진단 들어가기
    driver.switch_to.frame("TOBE_JSP")
    student = driver.find_element_by_xpath("""//*[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_7_cell_7_0_controltreeTextBoxElement"]/div""")
    student.click()

    tempCheck = driver.find_element_by_xpath("""//*[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_12_cell_12_0_controltreeTextBoxElement"]/div""")
    driver.implicitly_wait(5)
    tempCheck.click()

    # input에 36~37도 랜덤으로 들어가고 확인까지 눌러줌 그러고 파일 종료
    input = driver.find_element_by_id("mainframe_VFrameSet_HFrameSet_MDIFrameSet_ctxFrameSet_ctxFrame_PERS07^PERS07_08^005^AmcDailyTempRegE_form_div_sample_divMain_divForm_edtTemp_input")
    input.click()

    randTemp = str(36+round(random(),1))
    input.send_keys(randTemp)

    save = driver.find_element_by_id("""mainframe_VFrameSet_HFrameSet_MDIFrameSet_ctxFrameSet_ctxFrame_PERS07^PERS07_08^005^AmcDailyTempRegE_form_div_sample_divMain_btnSave""")
    save.click()
    time.sleep(3)

    result = driver.switch_to_alert()
    print(result.text)
    result.accept()
    now = datetime.datetime.now()
    print(f'등록시간: {now}')

    time.sleep(5)
    driver.quit()

userid = input('zeus id: ')
userpw = input('zeus pw: ')

# 최초 실행시 한 번 실행해줌
tempCheck()
# 12시간 마다 체온체크를 함
schedule.every(12).hours.do(tempCheck)

while True:
    schedule.run_pending()
    time.sleep(1)