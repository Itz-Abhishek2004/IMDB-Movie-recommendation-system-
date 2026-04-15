# scraper.py skeleton
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
movies = []

for start in range(1, 251, 50):  # 250 movies, 50 per page
    url = f"https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31&start={start}"
    driver.get(url)
    time.sleep(3)
    # scrape name + storyline
    # append to movies list

df = pd.DataFrame(movies, columns=["Movie Name", "Storyline"])
df.to_csv("movies_data.csv", index=False)
driver.quit()