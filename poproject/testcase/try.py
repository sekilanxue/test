import yaml
from selenium import webdriver

chrome_arg = webdriver.ChromeOptions()
chrome_arg.debugger_address = '127.0.0.1:9888'
driver = webdriver.Chrome(options=chrome_arg)
driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
driver.implicitly_wait(5)
driver.find_element_by_css_selector('#menu_contacts').click()
driver.find_element_by_css_selector('.jstree-node.js_editable.jstree-last.jstree-open').click()
ele_list_depart = driver.find_elements_by_css_selector(".jstree-anchor")
list_member = [i.text for i in ele_list_depart]
print(list_member)