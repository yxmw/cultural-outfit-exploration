# Reddit & Pinterest Cultural Outfit Exploration

Exploring multicultural wedding and festival outfits across Reddit and Pinterest —  
a cold-start SNS data exploration project focusing on both **technical implementation** and **cultural insight**.

## 🧠 Overview
This project simulates a *cold-start data exploration* scenario.  
It combines API-based and manual data collection to analyze cultural diversity,  
AI-generated content, and data bias in social media fashion datasets.

## 🛠️ Tools & Methods
- **Python:** `praw`, `pandas`, `tqdm`, `requests`
- **Platforms:** Reddit API, Pinterest (manual sampling)
- **Data:** Text, image URLs, keywords, cultural tags
- **Output:** `reddit_samples.csv`, `manual_search.csv`

## 📊 Key Insights
- Pinterest samples contain a high ratio of AI-generated or Western-dominant content.
- Reddit discussions provide more authentic and diverse cultural references.
- Multilingual keywords (e.g., *qipao*, *hanbok*, *lehenga*) help increase dataset diversity.
- Reflection included on researcher bias and data modality (image/video).

## 📁 Repository Contents
| File | Description |
|------|--------------|
| `reddit_api.py` | Reddit scraping script |
| `pinterest_api.py` | Pinterest sampling script |
| `reddit_samples.csv` | Reddit dataset |
| `manual_search.csv` | Pinterest dataset |
| `search_report.pdf` | Final analysis report |
| `README.md` | Project documentation |

## ⚠️ Note
For security reasons, API credentials (`client_id`, `client_secret`, `token`) are not included.  
Please insert your own credentials in the scripts before running.

---

📍 *Created by Maggie Wang | Oct 2025*
