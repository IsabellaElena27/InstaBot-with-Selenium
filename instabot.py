
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from credentials import username, password

# Install Webdriver
service = Service(ChromeDriverManager().install())

# Create Driver Instance
driver = webdriver.Chrome(service=service)

# Set the maximum amount of time to wait for elements
wait = WebDriverWait(driver, 10)

# Get Web Page
driver.get('https://www.instagram.com')

# Wait for and click the cookie acceptance button
cookie = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')))
cookie.click()

# Input username and password
username1 = username
password1 = password

username = driver.find_element(By.NAME, 'username')
username.send_keys(username1)

password = driver.find_element(By.NAME, 'password')
password.send_keys(password1)
password.submit()

# Wait for and click "Not Now" for notifications
notnow = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
notnow.click()

# Wait for and click "Turn Off" for notifications
turnoff = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                 '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
turnoff.click()

# Wait for and click the message icon
msg_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Direct"]')))
msg_element.click()

# Wait for and click "New Message"
svg_element2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="New message"]')))
svg_element2.click()

# Input name and click
type_name = wait.until(EC.presence_of_element_located((By.XPATH,
                                                       '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')))
type_name.send_keys('') # input name
chat_result = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                     '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div')))
chat_result.click()

# Wait for and click the "Chat" button
chat_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Chat"]')))
chat_button.click()

# Wait for and locate the message input element
p_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.xat24cr.xdj266r')))

# Input the message
message = 'This is a TEST!'
p_element.send_keys(message)

# Wait for and click the "Send" button
send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Send"]')))
send_button.click()
time.sleep(7)

# Close the browser
driver.quit()
