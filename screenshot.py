from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from time import sleep
import img2pdf

usernameStr = ''
passwordStr = ''

browser = webdriver.Chrome(r"C:\Users\Mario Autore\Downloads\chromedriver_win32\chromedriver.exe")
browser.get('https://learn.unimol.it/pluginfile.php/74518/mod_scorm/content/1/res/index.html')


username = browser.find_element_by_id('username')
username.send_keys(usernameStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)
nextButton = browser.find_element_by_class_name('form-button')
nextButton.click()
time.sleep(5)
nextButton1 = browser.find_element_by_class_name('universal-control-panel__button_right-arrow')
i=0
String1="screenshot"
String2=".png"
pdfname=""
while True:
    name = String1 + str(i) + String2
    pdfname=pdfname+"'"+name+"'"+","
    nextButton1.click()
    sleep(1)
    browser.get_screenshot_as_file(name)
    sleep(1)
    i=i+1

dirname = ""
imgs = []
for fname in os.listdir(dirname):
	if not fname.endswith(".png"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue
	imgs.append(path)
with open("name.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))





