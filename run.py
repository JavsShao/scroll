from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 输入问题
driver.find_element_by_id('kw').send_keys('葡萄')
# 点击搜索
driver.find_element_by_id('su').click()
# 查看初始快照
driver.save_screenshot("old.png")
# 等待5秒
time.sleep(5)
# 向下拖动至底
js = 'window.scrollTo(0, document.body.scrollHeight)'
driver.execute_script(js)
# 查看拉到底的快照
driver.save_screenshot("new.png")
