from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument('--no-sandbox')
Chrome_options.add_argument('--headless')
Chrome_options.add_argument('--disable-gpu')
Chrome_options.add_argument('--disable-dev-shm-usage')        


def getjoke(URL):
  Browser = webdriver.Chrome(options=Chrome_options)
  print('inicio joke_getter')
  Browser.get(URL)
  WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/h1')))
  print('parte2 joke getter')
  Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div').click()
  WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div')))
  element2 = Browser.find_element_by_xpath('/html/body/div[2]/div[3]/div').text
  Browser.close()
  return element2


def gethash(selecao, text):
  Browser = webdriver.Chrome(options=Chrome_options)
  test_list = ['md2','md4', 'md5', 'sha224', 'sha256', 'sha384', 'sha512']
  if selecao.lower() in test_list:
    print('inicio hash getter')
    Browser.get('https://www.tools4noobs.com/online_tools/hash/')
    WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/h1')))
    print('parte 2 hash')
    selection = Select(Browser.find_element_by_xpath('//*[@id="algo"]'))
    if selecao.lower() == 'md2':
      selection.select_by_value('md2')
      input_text = Browser.find_element_by_xpath('//*[@id="text"]')
      print(text)
      input_text.send_keys(text)
      print('done')
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form/div/input')))
      Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input').click()
      sleep(1)
      hashed_text = Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div').text
      Browser.close()
      return hashed_text
    elif selecao.lower() == 'md4':
      selection.select_by_value('md4')
      input_text = Browser.find_element_by_xpath('//*[@id="text"]')
      print(text)
      input_text.send_keys(text)
      print('done')
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form/div/input')))
      Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input').click()
      sleep(1)
      hashed_text = Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div').text
      Browser.close()
      return hashed_text

    elif selecao.lower() == 'md5':
      selection.select_by_value('md5')
      input_text = Browser.find_element_by_xpath('//*[@id="text"]')
      print(text)
      input_text.send_keys(text)
      print('done')
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form/div/input')))
      Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input').click()
      sleep(1)
      hashed_text = Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div').text
      Browser.close()
      return hashed_text

    elif selecao.lower() == 'sha224':
      selection.select_by_value('sha224')
      input_text = Browser.find_element_by_xpath('//*[@id="text"]')
      print(text)
      input_text.send_keys(text)
      print('done')
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form/div/input')))
      Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input').click()
      sleep(1)
      hashed_text = Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div').text
      Browser.close()
      return hashed_text

    elif selecao.lower() == 'sha256':
      selection.select_by_value('sha256')
      input_text = Browser.find_element_by_xpath('//*[@id="text"]')
      print(text)
      input_text.send_keys(text)
      print('done')
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form/div/input')))
      Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input').click()
      sleep(1)
      hashed_text = Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div').text
      Browser.close()
      return hashed_text

    elif selecao.lower() == 'sha384':
      selection.select_by_value('sha384')
      input_text = Browser.find_element_by_xpath('//*[@id="text"]')
      print(text)
      input_text.send_keys(text)
      print('done')
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form/div/input')))
      Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input').click()
      sleep(1)
      hashed_text = Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div').text
      Browser.close()
      return hashed_text

    elif selecao.lower() == 'sha512':
      selection.select_by_value('sha512')
      input_text = Browser.find_element_by_xpath('//*[@id="text"]')
      print(text)
      input_text.send_keys(text)
      print('done')
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/form/div/input')))
      Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input').click()
      sleep(1)
      hashed_text = Browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div').text
      Browser.close()
      return hashed_text


def gethash_and_enconding(selecao, text):
  Browser = webdriver.Chrome(options=Chrome_options)
  test_list = ['sha512/244','sha512/256', 'base32', 'base64', 'dbase32', 'dbase64']
  if selecao.lower() in test_list:
    print('inicio decode encode hash getter')
    Browser.get('https://emn178.github.io/online-tools/index.html')
    WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/h1/a')))
    if selecao.lower() == 'sha512/244':
      Browser.find_element_by_xpath('/html/body/div[2]/div/ul[1]/li[12]/a').click()
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/h1')))
      input_text = Browser.find_element_by_xpath('//*[@id="input"]')
      print(text)
      input_text.send_keys(text)
      print('aqui')
      Browser.find_element_by_xpath('//*[@id="execute"]').click()
      sleep(1)
      hashed_encoded_text = Browser.find_element_by_xpath('//*[@id="output"]').get_attribute('value')
      print(hashed_encoded_text)
      Browser.close()
      return hashed_encoded_text

    if selecao.lower() == 'sha512/256':
      Browser.find_element_by_xpath('/html/body/div[2]/div/ul[1]/li[13]/a').click()
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/h1')))
      input_text = Browser.find_element_by_xpath('//*[@id="input"]')
      print(text)
      input_text.send_keys(text)
      print('aqui')
      Browser.find_element_by_xpath('//*[@id="execute"]').click()
      sleep(1)
      hashed_encoded_text = Browser.find_element_by_xpath('//*[@id="output"]').get_attribute('value')
      print(hashed_encoded_text)
      Browser.close()
      return hashed_encoded_text

    if selecao.lower() == 'base32':
      Browser.find_element_by_xpath('/html/body/div[2]/div/ul[3]/li[2]/a').click()
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/h1')))
      input_text = Browser.find_element_by_xpath('//*[@id="input"]')
      print(text)
      input_text.send_keys(text)
      print('aqui')
      Browser.find_element_by_xpath('//*[@id="execute"]').click()
      sleep(1)
      hashed_encoded_text = Browser.find_element_by_xpath('//*[@id="output"]').get_attribute('value')
      print(hashed_encoded_text)
      Browser.close()
      return hashed_encoded_text

    if selecao.lower() == 'base64':
      Browser.find_element_by_xpath('/html/body/div[2]/div/ul[3]/li[4]/a').click()
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/h1')))
      input_text = Browser.find_element_by_xpath('//*[@id="input"]')
      print(text)
      input_text.send_keys(text)
      print('aqui')
      Browser.find_element_by_xpath('//*[@id="execute"]').click()
      sleep(1)
      hashed_encoded_text = Browser.find_element_by_xpath('//*[@id="output"]').get_attribute('value')
      print(hashed_encoded_text)
      Browser.close()
      return hashed_encoded_text
    
    if selecao.lower() == 'dbase32':
      print('BEGGIN')
      Browser.find_element_by_xpath('/html/body/div[2]/div/ul[4]/li[2]/a').click()
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/h1')))
      input_text = Browser.find_element_by_xpath('//*[@id="input"]')
      print(text)
      input_text.send_keys(text)
      print('aqui')
      Browser.find_element_by_xpath('//*[@id="execute"]').click()
      sleep(1)
      hashed_encoded_text = Browser.find_element_by_xpath('//*[@id="output"]').get_attribute('value')
      print(hashed_encoded_text)
      Browser.close()
      return hashed_encoded_text

    if selecao.lower() == 'dbase64':
      Browser.find_element_by_xpath('/html/body/div[2]/div/ul[4]/li[4]/a').click()
      WebDriverWait(Browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/h1')))
      input_text = Browser.find_element_by_xpath('//*[@id="input"]')
      print(text)
      input_text.send_keys(text)
      print('aqui')
      Browser.find_element_by_xpath('//*[@id="execute"]').click()
      sleep(1)
      hashed_encoded_text = Browser.find_element_by_xpath('//*[@id="output"]').get_attribute('value')
      print(hashed_encoded_text)
      Browser.close()
      return hashed_encoded_text
    