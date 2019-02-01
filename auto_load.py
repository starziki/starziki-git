import pyautogui as ag

ag.getWindowsWithTitle("Instagram - Chrome")[0].focus()
ag.moveTo(943,139)
ag.click()

search="#lottegiants"
for n in search:
    ag.press(n)

ag.press("enter")

ag.moveTo(919,225,2)
ag.click()

ag.moveTo(649,604,2)
ag.click()
ag.moveTo(1069,742,2)
ag.click()
ag.moveTo(1600,800)
ag.click()

ag.moveTo(293+649,604,2)
ag.click()
ag.moveTo(1069,742,2)
ag.click()
ag.moveTo(1600,800)
ag.click()

ag.moveTo(2*293+649,604,2)
ag.click()
ag.moveTo(1069,742,2)
ag.click()
ag.moveTo(1600,800)
ag.click()

ag.scroll(-604)
ag.moveTo(2*293+649,604,2)
ag.click()
ag.moveTo(1069,742,2)
ag.click()
ag.moveTo(1600,800)
ag.click()

ag.moveTo(470,138)
ag.click()

