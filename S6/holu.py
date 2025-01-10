from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # falta en rasbery
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




drive = webdriver.chrome
if drive :
    print("asd")
else :
    print ("holuu")
