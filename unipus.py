from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time
import config
import four as unipus
from selenium.common.exceptions import TimeoutException


# 指定chromedriver的路径
webdriver_service = Service(config.user.chormedriverlocation)

# 指定Chrome的路径
chrome_options = Options()
chrome_options.binary_location = config.user.chormelocation

# 创建一个新的Chrome浏览器实例
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# 让浏览器打开目标网页
driver.get(r"https://sso.unipus.cn/sso/login?service=https%3A%2F%2Fu.unipus.cn%2Fuser%2Fcomm%2Flogin")
# 搜索name="username"的元素，定位到账号输入框
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
username = driver.find_element(By.NAME, "username")
# 输入账号
username.send_keys(config.user.username)
# 搜索name="password"的元素，定位到密码输入框
password = driver.find_element(By.NAME, "password")
# 输入密码
password.send_keys(config.user.password)
# 勾选所有<input type="checkbox">
checkbox = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for i in checkbox:
    i.click()
# 搜索id="login"的元素，定位到登录按钮
login = driver.find_element(By.ID, "login")
login.click()

input("按Enter继续...")
currenturl = driver.current_url
#截取url井号之前的部分（包括井号）
urlprefix = currenturl.split("#")[0]

for i in unipus.exercises:
    # 用户手动在命令行输入时向下进行

    #url拼接
    url = urlprefix + i.url
    print (url)
    #让浏览器打开目标网页
    driver.get(url)
    try:
        button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(),'确定')]]")))
        button.click()
    except TimeoutException:
        pass
    #使用正则匹配当前url
    answer = i.answer
    # for i in unipus.exercises:
    #     print (i.url , currenturl)
    #     print (re.search(i.url, currenturl))
    #     if re.search(i.url, currenturl):
    #         answer = i.answer
    #         break
    #     else:
    #         continue
    # if answer == "":
    #     print("未找到对应答案")
    #     continue
    answer = answer.replace("(", " ")
    answer = answer.replace(")", " ")
    answer = answer.replace("（", " ")
    answer = answer.replace("）", " ")
    answer= answer.replace(".", " ")
    answer = re.sub('\d+', ' ', answer)
    # answer = answer.replace("\r", "").replace("\n", "")
    #按照空格分割字符串
    answer = answer.replace("\n\n", "\n")
    # answer = answer.replace("\n", "")
    answer = answer.split("\n")
    answer = [i for i in answer if i]  # 移除空字符串
    for i in range(len(answer)):
        print (answer[i])
    # 等待页面加载完成
    try:
        submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'提交')]")))
    except TimeoutException:
        print("页面加载失败")
    # 搜索所有<input type="text">
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for i in range(len(inputs)):
        inputs[i].send_keys(answer[i])
        pass
    
    #搜索<button>提交</button>
    # input("Press Enter to continue...")
    submit = driver.find_element(By.XPATH, "//button[contains(text(),'提交')]")
    submit.click()
    time.sleep(1)
    #搜索确认提交的<button>确认</button>
    # if WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//button//div//div//span[contains(text(),'确认')]"))) != None:
    #     submit_confirm = driver.find_element(By.XPATH, "//button//div//div//span[contains(text(),'确认')]")
    #     submit_confirm.click()
    try:
        submit_confirm = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//button//div//div//span[contains(text(),'确认')]")))
        submit_confirm.click()
    except TimeoutException:
        pass
    time.sleep(1)
    # 用户手动在命令行输入时向下进行
    # input("Press Enter to continue...")
input ("按Enter退出...")
