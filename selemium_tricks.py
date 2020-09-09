### Select element based on text
"""
el = driver.find_element_by_xpath("//*[text()='Exact Match']")
el = driver.find_element_by_xpath("//*[contains(text(), 'Partial Match')]")

loginButton = browser.find_element(By.XPATH, "//*[@value='Log In']")
"""
