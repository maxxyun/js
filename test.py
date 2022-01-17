from selenium import webdriver

url = "https://play.google.com/store/apps/details?id=kr.co.zumo.app&showAllReviews=true"
driverPath = "../02.App_review/config/chromedriver_win32/chromedriver.exe"  # driver file path
driver = webdriver.Chrome(driverPath)
driver.get(url)