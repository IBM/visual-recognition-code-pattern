import os, time, sys, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Do an action on the app's landing page
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.get(os.environ.get("APP_URL", "http://localhost:5000/")); # Open a browser to the app's landing page

time.sleep(3) # Init time needed?

try:
  driver.find_element_by_class_name('react-json-view')
except NoSuchElementException:
  pass
else:
  print("Found the JSON view before it was expected")
  sys.exit("Experience Test Failed")

# Press the button
json_button = driver.find_element_by_xpath("//button/span[contains(text(),'JSON')]") # Locate the button
json_button.click()

json_view = driver.find_element_by_class_name('react-json-view')
json_view_text = json_view.text

# Simplistic check for something like this in the JSON:
# 4:{
# "class":"tweed"
# "score":0.791
# "type_hierarchy":"/fabric/tweed"
# }
expected = "/fabric/tweed"
if expected in json_view_text:
    print("Tweed JSON Test Successful")
else:
    sys.exit("Experience Test Failed")

# Click an image tile
computer_chip = driver.find_element_by_id('tile-1')
clickable = computer_chip.find_element_by_xpath('..')
clickable.click()

time.sleep(3)
json_view = driver.find_element_by_class_name('react-json-view')
json_view_text = json_view.text

expected = "electrical device"
if expected in json_view_text:
    print("Chip JSON Test Successful")
else:
    sys.exit("Experience Test Failed")

print("Experience Test Successful")
