# -*- coding: UTF-8 -*-
from selenium import webdriver
b= webdriver.Firefox()
b.get("http://www.maiziedu.com")
b.maximize_window()
url0 = b.current_window_handle
print(url0)
#ele = b.find_element_by_link_text('Python全栈开发')
ele = b.find_element_by_partial_link_text("开发")
ele.click()
b.implicitly_wait(30)

for handle in b.window_handles:
    b.switch_to.window(handle)
url = b.current_window_handle
print(url)
ele2 = b.find_element_by_css_selector("input[id=\"data-search\"]")

ele2.click()
ele2.send_keys("python")
b.back()

