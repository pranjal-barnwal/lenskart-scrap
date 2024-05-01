from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv

url = "https://www.lenskart.com/eyeglasses.html?product_type=Eyeglasses"

driverPath = "C:/Program Files/chromedriver/chromedriver.exe"
srvc = Service(driverPath)

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=srvc, options=opts)
driver.maximize_window()
driver.get(url)

time.sleep(3)
height=driver.execute_script("return document.body.scrollHeight")
newHeight=500

while True:
    driver.execute_script("window.scrollTo(0, arguments[0])", newHeight)
    time.sleep(1)
    currHeight = driver.execute_script("return document.body.scrollHeight")
    newHeight += 500
    # if height== newHeight:
    #     break
    if currHeight <= newHeight:
        break
#. Scrolled till very end


items = driver.find_elements(By.CLASS_NAME, "AnchorWrapper--1smmibb")
print(len(items))

# Create a CSV file to write the data
with open("eyeglasses.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Size", "Price"])  # Write header row

    # Loop through each item and extract the data
    for item in items:
        # Extract title
        title = item.find_element(By.CLASS_NAME, "ProductTitle--13we1dx").text.strip()

        # # Extract Size
        size = item.find_element(By.CLASS_NAME, "ProductSize--64lzs8").text.strip()

        # # Extract Price
        price = item.find_element(By.CLASS_NAME, "SpecialPriceSpan--1olt47v").text.strip()

        # # Extract Image URL
        # imgUrl = item.find_element(By.CLASS_NAME, "ProductImage--xka74 HxzMC").get_attribute("src").text.strip()


        # Write data to CSV file
        writer.writerow([title, size, price])
        # writer.writerow([title, size, price, imgUrl])

        arr = [title, size, price]
        print(arr)

# Close the browser
driver.quit()
