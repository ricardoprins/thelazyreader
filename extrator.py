from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = r'C:\Users\hap\Documents\webdriver\chromedriver.exe' # Onde esta o seu driver no computador
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")

busca = driver.find_element_by_name('q')
busca.send_keys('microsoft')
busca.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    results = main.find_elements_by_class_name("yuRUbf")

    for result in results:
        link = result.find_element_by_tag_name('a')
        print(link.get_property('href'))
    

finally:
    driver.quit()