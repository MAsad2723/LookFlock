from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# URL of the website
url = "https://www.gulahmedshop.com/sale?discount_percentage=7735"

# Open the website
driver.get(url)

# Define a function to scroll to the bottom of the page
def scroll_to_bottom(driver):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(5)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Define a function to click the "Load more" button
def click_load_more(driver):
    try:
        load_more_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ias-trigger ias-trigger-next']//a[contains(text(),'Load more')]"))
        )
        load_more_button.click()
        return True
    except:
        print("No more 'Load More' button found.")
        return False

# Call function to scroll to the bottom of the page
scroll_to_bottom(driver)

# Keep clicking the "Load more" button until it's no longer available
while click_load_more(driver):
    time.sleep(5)  # Wait for the newly loaded content to render

# Parse the HTML content
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all product items
product_items = soup.find_all('div', class_='product-item-info')
# print(product_items)
# Define lists to store data
product_names = []
image_urls = []
current_prices = []
old_prices = []
discounts = []

# Iterate over product items
for item in product_items:
    # Product Name
    product_name_tag = item.find('span', class_='product-item-link')
    product_names.append(product_name_tag.text.strip() if product_name_tag else None)

    # Image URL
    
    # image_tag = item.find('div', class_='item')
    # image = image_tag.find('img', class_='')
    # image_urls.append(image['src'] if image_tag else None)
    # print(image_tag)    
    slick_current = item.find('div', class_='slick-current')
    div = slick_current.find('div', class_='') if slick_current else None
    items = div.find('div', class_='item') if div else None
    image = items.find('img', class_='') if items else None
    image_urls.append(image['src'] if image else None)
    
    # Current Price
    current_price_tag = item.find('span', class_='special-price')
    current_price = current_price_tag.find('span', class_='price').text.strip() if current_price_tag else None
    current_prices.append(current_price)

    # Old Price
    old_price_tag = item.find('span', class_='old-price')
    old_price = old_price_tag.find('span', class_='price').text.strip() if old_price_tag else None
    old_prices.append(old_price)

    # Discount
    discount_tag = item.find('div', class_='save-price-wrapper')
    discount = discount_tag.find('span', class_='price').text.strip() if discount_tag else None
    discounts.append(discount)
    time.sleep(1)

# Close the WebDriver
time.sleep(5)
driver.quit()

# Write scraped data to a file
with open("scraped_data.txt", "w") as file:
    for i in range(len(product_names)):
        file.write('{')
        file.write('"id": "{}",\n'.format(i+1))
        file.write('"name": "{}",\n'.format(product_names[i]))
        file.write('"imageURL": "{}",\n'.format(image_urls[i]))
        file.write('"currentPrice": {},\n'.format(current_prices[i]))
        file.write('"oldPrice": {},\n'.format(old_prices[i]))
        file.write('"discount": {}"\n'.format(discounts[i]))
        file.write("\n")
        file.write('}')

print("Scraped data has been saved to 'scraped_data.txt'")
