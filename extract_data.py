from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import csv
from urllib.parse import urlparse, parse_qs

chrome_options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

csv_filename = 'links.csv'
links = []
with open(csv_filename, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        links.append(row[0])

output_csv_filename = 'extracted_data.csv'
with open(output_csv_filename, 'w', newline='', encoding='utf-8') as output_csv:
    csv_writer = csv.writer(output_csv)
    csv_writer.writerow(['Name', 'Type', 'Location', 'Latitude', 'Longitude'])

    for link in links:
        driver.get(link)
        sleep(2)
        
        name = driver.find_element(By.CSS_SELECTOR, 'span[data-original-title=""][title=""]').text
        highlight_type = driver.find_element(By.CSS_SELECTOR, 'p.tw-text-secondary').text
        location = driver.find_element(By.CSS_SELECTOR, 'p.css-6jypgg').text
        specific_link = driver.find_element(By.CLASS_NAME, 'css-yd1dt0')
        
        href = specific_link.get_attribute('href')
        lat_lng_start = href.find('@') + 1
        lat_lng_end = href.find('/', lat_lng_start)
        lat_lng_str = href[lat_lng_start:lat_lng_end]
        latitude, longitude = map(float, lat_lng_str.split(','))

        csv_writer.writerow([name, highlight_type, location, latitude, longitude])

driver.quit()
print(f"Data saved in {output_csv_filename}")
