from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import csv
import sys
komoot_url = sys.argv[1]

chrome_options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(komoot_url)
sleep(5)
button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="gdpr-banner-accept"]')
button.click()

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    if driver.execute_script("return (window.innerHeight + window.scrollY) >= document.body.scrollHeight;"):
        break

links = driver.find_elements(By.CSS_SELECTOR, 'a[data-test-id="highlights_list_item_title"]')
csv_filename = 'links.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Link'])

    for link in links:
        href = link.get_attribute('href')
        csv_writer.writerow([href])

print(f'Links saved in {csv_filename}')
driver.quit()
