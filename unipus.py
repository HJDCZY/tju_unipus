from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

# 指定chromedriver的路径
webdriver_service = Service('chromedriver.exe')

# 指定Chrome的路径
chrome_options = Options()
chrome_options.binary_location = 'E:\\chrome-win64\\chrome.exe'

# 创建一个新的Chrome浏览器实例
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# 让浏览器打开目标网页
driver.get(r"https://sso.unipus.cn/sso/login?service=https%3A%2F%2Fu.unipus.cn%2Fuser%2Fcomm%2Flogin")
# 搜索name="username"的元素，定位到账号输入框
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
username = driver.find_element(By.NAME, "username")
# 输入账号
username.send_keys("13116033570")
# 搜索name="password"的元素，定位到密码输入框
password = driver.find_element(By.NAME, "password")
# 输入密码
password.send_keys("Yoyo14185721")
# 勾选所有<input type="checkbox">
checkbox = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for i in checkbox:
    i.click()
# 搜索id="login"的元素，定位到登录按钮
login = driver.find_element(By.ID, "login")
login.click()

while True:
    # 用户手动在命令行输入时向下进行
    input1 = input("输入ok继续：")
    while input1 != "ok":
        input1 = input("输入ok继续：")
    file = open("1.txt", "r")
    #消除文件中的数字和左右括号和.
    input2 = file.read()
    input2 = input2.replace("(", "")
    input2 = input2.replace(")", "")
    input2= input2.replace(".", "")
    input2 = re.sub('\d+', '', input2)
    # input2 = input2.replace("\r", "").replace("\n", "")
    #按照换行符分割字符串
    input2 = input2.replace("\n\n", "\n")
    input2 = input2.split("\n")
    input2 = [i for i in input2 if i]  # 移除空字符串
    for i in range(len(input2)):
        print (repr(input2[i]))
        print ("------------------")
    # 搜索所有<input type="text">
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for i in range(len(inputs)):
        inputs[i].send_keys(input2[i])
        pass
    file.close()
    # 用户手动在命令行输入时向下进行
        



