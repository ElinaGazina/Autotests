# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By ##https://habr.com/ru/articles/250975/


link = "https://www.youtube.com/" #обьявили переменную и в нее поместили нашу ссылку

try:
    browser = webdriver.Chrome()
    browser.get(link) # сделали запрос по нашей ссылке
    input_1 = browser.find_element(By.CSS_SELECTOR, value='input#search')
    input_1.send_keys("Python Selenium Pytest Series") #вводин нашу поисковую фразу
    time.sleep(1) #задержка 1 секунжа
    input_1.submit() #что типо энтэра
    button_2 = browser.find_element(By.CSS_SELECTOR, value= '#content > a')
    button_2.click() #клик
finally:
    # задержка 30 секунд
    time.sleep(30)
    browser.quit()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
