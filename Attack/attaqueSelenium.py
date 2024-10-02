from asyncio import *
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

start = time.time()
browser = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.options import Options

browser.get("http://127.0.0.1:9009")

browser.find_element("id",'username').send_keys("fateh")

time.sleep(3)


def Afficher_Cas_possible(ensemble, k):
 
    n = len(ensemble)
    Afficher_Cas_possibleRec(ensemble, "", n, k)

def Afficher_Cas_possibleRec(ensemble, code, n, k):
    if (k == 0) :
        browser.find_element("id",'password2').send_keys(code)
        end = time.time()
        print(f"Le temps d'execution est: {end - start} secondes")
        browser.find_element("id",'submit').click()
        sleep(1)
        return
 
    for i in range(n):
        newcode = code + ensemble[i]
        Afficher_Cas_possibleRec(ensemble, newcode, n, k - 1)


ensemble2 = ['0', '1', '2', '3','4','5', '6', '7','8','9']
k = 5
Afficher_Cas_possible(ensemble2, k)




chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

while True:
    sleep(1)

