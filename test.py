from selenium import webdriver
chrome= webdriver.Chrome()

chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_elements_by_link_text("Button")[3].click()
chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_elements_by_xpath('//div[@class="et_pb_column et_pb_column_1_2 et_pb_column_8    et_pb_css_mix_blend_mode_passthrough"]//a[@title="Follow on Facebook"]')[1].click()
chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_element_by_id("s").send_keys("HI!")
chrome.find_element_by_xpath('//div[@id="search-2"]//input[@id="searchsubmit"]').click()
chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_element_by_id("et_pb_contact_name_0").send_keys("Nataly")
chrome.find_element_by_id("et_pb_contact_email_0").send_keys("gleam777@gmail.com")
chrome.find_element_by_id("et_pb_contact_message_0").send_keys("Everything is good!:)")
chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_element_by_xpath('//form[@id="subscribe-blog-blog_subscription-2"]//input[@name="email"]').send_keys("gleam777@gmail.com")
chrome.find_element_by_xpath('//p[@id="subscribe-submit"]//button[@name="jetpack_subscriptions_widget"]').click()
chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//input[@name="log"]').send_keys("gleam777@gmail.com")
chrome.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//input[@name="pwd"]').send_keys("1111")
chrome.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//button[@class="et_pb_newsletter_button et_pb_button"]').click()
chrome.get("https://www.ultimateqa.com/complicated-page/")