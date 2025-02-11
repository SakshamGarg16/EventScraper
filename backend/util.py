from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

MONGO_URI = "mongodb+srv://22052500:dummy@webscrapping.8xrmo.mongodb.net/?retryWrites=true&w=majority&appName=WebScrapping"
client = MongoClient(MONGO_URI)
db = client["eventsDB"]
events_collection = db["events"]



def scrape_events():
    """Scrapes event data from Eventbrite using Selenium and stores it in MongoDB."""
    
    # Configure Selenium to run headless (no GUI)
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")  
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage")  

    # Launch Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Load the Eventbrite Sydney events page
    driver.get("https://www.eventbrite.com.au/d/australia--sydney/all-events/")
    time.sleep(5)  # Wait for JavaScript to load
    
    event_list = []

    events = driver.find_elements(By.CLASS_NAME, "SearchResultPanelContentEventCardList-module__map_experiment_event_card___vyRC3")
    print(len(events))
    for event in events:
        try:
            title_element = event.find_element(By.TAG_NAME, "h3")
            date_element = event.find_elements(By.TAG_NAME, "p")
            link_element = event.find_element(By.TAG_NAME, "a")
            
            
            date = None
            for p in date_element:
                text = p.text.strip()
                if any(char.isdigit() for char in text):
                    date = text
                    break 

            if not date:
                date = "Soon"
                continue
            
            print(date)
            title = title_element.get_attribute("innerText").strip()           
            # date = date_element.get_attribute("innerText").strip()
            link = link_element.get_attribute("href")

            event_data = {
                "title": title,
                "date": date,
                "link": link
            }
            event_list.append(event_data)
        except Exception as e:
            print(f"Error extracting event: {e}")
    
    # Close the browser
    driver.quit()

    # Store in MongoDB
    if event_list:
        events_collection.drop()  # Clear old data
        events_collection.insert_many(event_list)

    print(f"Scraped {len(event_list)} events")  # Debugging
    return event_list

