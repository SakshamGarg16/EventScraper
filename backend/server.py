from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
import util


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

@app.get("/scrape")
def scrape():
    """Manually trigger scraping"""
    events = util.scrape_events()
    print(events)
    return {"message": "Events scraped successfully", "events": events}

@app.get("/events")
def get_events():
    """Fetch events from MongoDB"""
    events = list(events_collection.find({}, {"_id": 0}))
    return {"events": events}

# Schedule event scraping every 24 hours
scheduler = BackgroundScheduler()
scheduler.add_job(util.scrape_events, "interval", hours=24)
scheduler.start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
