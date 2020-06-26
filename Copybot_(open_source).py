from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

# General comments about the code:
# Everything that has "browser.find_element_by..." can be set to what best fits the HTML, usually xpath.
# For all functions the arguments passed in must be strings. Example below 
# user_login("UserID", "UserPW", "login", "John Smith", "ILoveCS123")
# For the function "get_data" it is highly reccomended to find elements by xpath since it allows
# the user to get all elements that have something in common, even if it's just a tag, like the following HTML:
# <b>lorem ipsum</b>. By inputting "//b" in the xpath you can find these elements that have few traits.
# The functions are executed at the bottom of the code.

browser = webdriver.YourWebdriver()
browser.get("Your desired link")

def user_login(userelement, passwordelement, loginelement, username, password):
    browser.implicitly_wait(5)
    usernametxtbox = browser.find_element_by_name(userelement) 
    passwordtxtbox = browser.find_element_by_name(passwordelement)
    loginbtn = browser.find_element_by_tag_name(loginelement)
    usernametxtbox.send_keys(username)
    passwordtxtbox.send_keys(password)
    webdriver.ActionChains(browser).move_to_element(loginbtn).click(loginbtn).perform()

# This next part is general website navigation to get to where the desired elements you want to fetch are.
# If upon login you have already reached the page, this part is unnecessary and can be deleted or commented.
# For navigation, you may add as many arguments as necessary to pass through each node.
def website_navigation(node1, node2, node3):
    browser.implicitly_wait(5)
    wantednode1 = browser.find_element_by_link_text(node1)
    webdriver.ActionChains(browser).move_to_element(wantednode1).click(wantednode1).perform()

    browser.implicitly_wait(5)
    wantednode2 = browser.find_element_by_css_selector(node2)
    webdriver.ActionChains(browser).move_to_element(wantednode2).click(wantednode2).perform()

    browser.implicitly_wait(5)
    wantednode3 = browser.find_element_by_xpath(node3)
    webdriver.ActionChains(browser).move_to_element(wantednode3).click(wantednode3).perform()
  
data = []
def get_data(location_of_elements, attribute_wanted): 
    datapoints = browser.find_element_by_xpath(location_of_elements)
    data.append(datapoints)
    for my_datapoint in datapoints:
       print(my_datapoint.get_attribute(attribute_wanted))
       data.append(my_datapoint.get_attribute(attribute_wanted))

def write_to_excel(name_of_column, path):
    document = pd.DataFrame(data = data, columns = [name_of_column])
    document.to_csv(path)


user_login()
# The code below is just in case a new tab pops up, 
# it was error handling for the website for which this program was created. By default it is commented,
# as it is likely a new tab won't pop up on most websites when a user logs in. 
# browser.switch_to.window(browser.window_handles[1])
# browser.close()
# browser.switch_to.window(browser.window_handles[0])
website_navigation()
# Most likely the site where you want to get data from will not have an iframe,
# so line 69 can be commented or erased. However, the site this program was originally inteded for had an iframe
# which took me, as a developer, a long time to realize and get around, so as a tribute to other new developers
# like me, line 69 has been left in but commented.
# browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
get_data()
write_to_excel()