from Driver import *
from random import random
from math import floor
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

keyword = "ร้านตัดผม+พญาไท"
rand = str(floor(random()*100))
rand2= str(floor(random()*100))
driver = createDriver(site = f"https://www.google.com/maps/search/{keyword}/@13.68417{rand},100.34130{rand2},15z",results=True,size="max")
focus = driver.find_elements(By.CLASS_NAME,"m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd")[1]
# driver.execute_script("arguments[0].focus();", focus)
a = ActionChains(driver)
a.move_to_element_with_offset(focus, 20,20)
a.click()
a.pause(2)
a.click()
for i in range(100):
    a.send_keys(Keys.SPACE)
    a.pause(0.5)
a.perform()
# sleep(10)
# driver.quit()