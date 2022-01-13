from selenium import webdriver

PATH = "/Library/chromedriver" #path for your chromedriver
driver = webdriver.Chrome(PATH)

driver.get("https://www.nasdaq.com/market-activity/stocks/screener")
i = 0

for price in driver.find_elements_by_tag_name("td"):
    print(price.text)

    i += 1

    if i == 48:
        break

driver.quit()
