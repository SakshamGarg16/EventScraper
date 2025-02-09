from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URI = "mongodb+srv://22052500:dummy@webscrapping.8xrmo.mongodb.net/?retryWrites=true&w=majority&appName=WebScrapping"
client = MongoClient(MONGO_URI)
db = client["eventsDB"]
events_collection = db["events"]

EVENT_URL = "https://www.sydney.com/events/"



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

    # Find event elements
    events = driver.find_elements(By.CLASS_NAME, "discover-event-card-wrapper")

    for event in events:
        try:
            title_element = event.find_element(By.CLASS_NAME, "discover-event-card-title")
            date_element = event.find_element(By.CLASS_NAME, "discover-event-card-date")
            link_element = event.find_element(By.TAG_NAME, "a")

            title = title_element.text.strip()
            date = date_element.text.strip()
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


@app.get("/scrape")
def scrape():
    """Manually trigger scraping"""
    events = scrape_events()
    return {"message": "Events scraped successfully", "events": events}

@app.get("/events")
def get_events():
    """Fetch events from MongoDB"""
    events = list(events_collection.find({}, {"_id": 0}))
    return {"events": events}

# Schedule event scraping every 24 hours
scheduler = BackgroundScheduler()
scheduler.add_job(scrape_events, "interval", hours=24)
scheduler.start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
