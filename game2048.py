from directkeys import PressKey, W, A, S, D
from selenium import webdriver
import process_img
import math
def startGame():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.set_window_position(-210, -450)
    driver.get("https://gabrielecirulli.github.io/2048/")
    appNotice = driver.find_element_by_class_name("app-notice")
    while(not appNotice.is_displayed()) :
        continue
    return driver

def doAction(driver, input_actions, gameStep):
    reward = 0.1
    terminal = False
    oldScore = int(driver.find_element_by_class_name("best-container").get_attribute('innerHTML'))
    if input_actions[0] == 1:
        PressKey(W)
        gameStep = gameStep + 1
    if input_actions[1] == 1:
        PressKey(A)
        gameStep = gameStep + 1
    if input_actions[2] == 1:
        PressKey(S)
        gameStep = gameStep + 1
    if input_actions[3] == 1:
        PressKey(D)
        gameStep = gameStep + 1

    gameImage = process_img.process_img()
    currentScore = int(driver.find_element_by_class_name("best-container").get_attribute('innerHTML'))
    retry = driver.find_element_by_class_name("retry-button")
    if(currentScore == 0):
        reward = 0
    elif(currentScore == oldScore) :
        reward = -1
    elif (currentScore > oldScore) :
        reward = (currentScore - oldScore) * math.log1p(gameStep) / 2048

    if(retry.is_displayed()):
        terminal = True
        reward = -1
        retry.click()
        gameStep = 0
    return gameImage, reward, terminal, gameStep