from directkeys import PressKey, W, A, S, D

import process_img
import math
def startGame(driver):
    driver.get("file:///C:/Users/pc/Documents/2048DQN/2048/index.html")
    return driver

def doAction(driver, input_actions, gameStep, oldScore):
    reward = 0.1
    terminal = False
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
    currentScore = int(driver.find_element_by_class_name("score-container").get_attribute('innerHTML').split('<',1)[0])
    retry = driver.find_element_by_class_name("retry-button")
    if(currentScore == 0):
        reward = 0
    elif(currentScore == oldScore) :
        reward = 0
    elif (currentScore > oldScore) :
        reward = 1
    oldScore = currentScore
    if(retry.is_displayed()):
        terminal = True
        reward = -1
        retry.click()
        gameStep = 0
    return gameImage, reward, terminal, gameStep, oldScore