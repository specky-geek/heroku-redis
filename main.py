from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

search_url=“https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568" 

driver.get(search_url.format(q='Car'))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5

imgResults = driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")
totalResults=len(imgResults)


img_urls = set()
for i in  range(0,len(imgResults)):
  img=imgResults[i]
  try:
    img.click()
    time.sleep(2)
    actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
    for actual_image in actual_images:
      if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):
        img_urls.add(actual_image.get_attribute('src'))
    print(img_urls)
  except ElementClickInterceptedException or ElementNotInteractableException as err:
    print(err)

print('done')
