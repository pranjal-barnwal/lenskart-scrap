import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "https://stores.lenskart.com/open-stores-list"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# getting the 1st table
tables = soup.find_all("table", class_="table table-hover")

# finding the required headers
headers_list = []
headers = tables[0].find_all("th")

    
# building the DataFrame
df = pd.DataFrame(columns=headers_list)
# print(df)


# Create a CSV file to write the data
with open("stores.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["StoreName", "City", "Phone", "Map"])  # Write header row

    for table in tables:
        rows = table.find_all("tr")

        for row in rows[1:]:
            cellsInRow = row.find_all("td")
            rowData = [cell.text.strip() for cell in cellsInRow]
            store_name = rowData[0]
            city = rowData[1]
            phone = rowData[4]
            map = cellsInRow[6].find("a")["href"]
    
        
        # Write data to CSV file
        writer.writerow([store_name, city, phone, map])
        
            
