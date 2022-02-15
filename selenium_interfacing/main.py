from selenium import webdriver

chrome_path="E:\development\Chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_path)
driver.get("https://www.amazon.com")
driver.close()