# 🎉 Sydney Events Scraper

[![GitHub issues](https://img.shields.io/github/issues/SakshamGarg16/EventScraper)](https://github.com/SakshamGarg16/EventScraper/issues)
[![GitHub forks](https://img.shields.io/github/forks/SakshamGarg16/EventScraper)](https://github.com/SakshamGarg16/EventScraper/network)
[![GitHub stars](https://img.shields.io/github/stars/SakshamGarg16/EventScraper)](https://github.com/SakshamGarg16/EventScraper/stargazers)
[![License](https://img.shields.io/github/license/SakshamGarg16/EventScraper)](LICENSE)

## 🚀 Project Overview
Sydney Events Scraper is a web application that scrapes event data for Sydney, Australia, and displays it in a user-friendly UI. Users can explore events and purchase tickets directly.

## 🎯 Features
- ✅ **Real-time Web Scraping** - Fetches up-to-date event details every 24 hours
- ✅ **User-friendly UI** - Built with React.js and TailwindCSS
- ✅ **Interactive Animations** - Engaging UI with animated backgrounds
- ✅ **MongoDB Atlas** - Cloud database storage for event details
- ✅ **CI/CD with GitHub Actions** - Automates deployments


## 🔧 Tech Stack
- **Frontend:** React.js, TailwindCSS
- **Backend:** FastAPI
- **Database:** MongoDB Atlas
- **Scraping:** BeautifulSoup, Requests
- **Deployment:** Docker, Kubernetes, Vercel

## 📌 Installation

1️⃣ **Clone the repository**
```sh
 git clone https://github.com/SakshamGarg16/EventScraper.git
 cd EventScraper
```

2️⃣ **Backend Setup**
```sh
 cd backend
 pip install -r requirements.txt
 uvicorn main:app --reload
```

3️⃣ **Frontend Setup**
```sh
 cd frontend
 npm install
 npm start
```

4️⃣ **Access the App:**
Open `http://localhost:3000/` in your browser.

## 📡 API Endpoints
| Method | Endpoint        | Description             |
|--------|----------------|-------------------------|
| GET    | `/events`       | Fetch all events       |
| POST   | `/scrape`       | Trigger scraping       |

## 📅 Roadmap
- [ ] Integrate AI-based event recommendations
- [ ] Add filtering & sorting options
- [ ] Implement user authentication

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
1. Fork the repo 🍴
2. Create a new branch 🌿
3. Commit your changes ✅
4. Open a Pull Request 🚀

### 🌟 Show Some Love!
If you like this project, **give it a star ⭐ on GitHub!**

---
🔗 **Follow me on GitHub:** [@SakshamGarg16](https://github.com/SakshamGarg16)

