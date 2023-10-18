```python
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get('http://localhost:8069')

# Define the screen sizes for testing
screen_sizes = {
    "mobile": (375, 812),
    "tablet": (768, 1024),
    "desktop": (1366, 768)
}

# Iterate over the screen sizes and test the responsiveness
for device, size in screen_sizes.items():
    driver.set_window_size(size[0], size[1])
    print(f"Testing on {device} device with size {size}")

    # Check if the header is displayed correctly
    assert driver.find_element(By.ID, 'headerNav').is_displayed()

    # Check if the main announcement is displayed correctly
    assert driver.find_element(By.ID, 'mainAnnouncement').is_displayed()

    # Check if the service icons are displayed correctly
    assert driver.find_element(By.ID, 'serviceIcons').is_displayed()

    # Check if the trending now section is displayed correctly
    assert driver.find_element(By.ID, 'trendingNow').is_displayed()

    # Check if the most popular games section is displayed correctly
    assert driver.find_element(By.ID, 'mostPopular').is_displayed()

    # Check if the explore our catalog section is displayed correctly
    assert driver.find_element(By.ID, 'exploreCatalog').is_displayed()

    # Check if the categories section is displayed correctly
    assert driver.find_element(By.ID, 'categories').is_displayed()

    # Check if the weekly deals section is displayed correctly
    assert driver.find_element(By.ID, 'weeklyDeals').is_displayed()

    # Check if the pre-order games section is displayed correctly
    assert driver.find_element(By.ID, 'preOrderGames').is_displayed()

    # Check if the testimonials section is displayed correctly
    assert driver.find_element(By.ID, 'testimonials').is_displayed()

    # Check if the latest news section is displayed correctly
    assert driver.find_element(By.ID, 'latestNews').is_displayed()

    # Check if the footer is displayed correctly
    assert driver.find_element(By.ID, 'footer').is_displayed()

print("All tests passed successfully!")

# Close the browser
driver.quit()
```