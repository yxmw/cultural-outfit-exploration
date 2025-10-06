from datetime import datetime, timezone
from tqdm import tqdm
import pandas as pd
import praw


# set up
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    user_agent="cold-start-sns/0.1 by USERNAME"
)
print("read_only:", reddit.read_only)

'''
for post in reddit.subreddit("weddingdress").hot(limit=5):
    print(post.id, post.title, post.url)

SUBREDDITS = ["weddingplanning","wedding","weddingdress","hanfu","IndianFashion","AsianBeauty"]
KEYWORDS = ["wedding dress", "wedding", "saree","hanfu","kimono","ankara","qipao"]
'''

SEARCH_PLAN = {
    "weddingdress": ["dress", "wedding dress", "asian", "indian", "pakistani", "hanfu", "saree", "kimono", "ankara", "qipao"],
    "wedding": ["dress", "wedding dress", "asian", "indian", "pakistani", "hanfu", "saree", "kimono", "ankara", "qipao"],
    "weddingplanning": ["dress", "wedding dress", "hanfu", "saree", "kimono", "ankara", "qipao"],
    "AsianBeauty": ["wedding", "wedding dress", "bride"],
    "IndianFashion": ["wedding dress", "wedding"],
}



# extraction
def extract_image(sub):
    
    if sub.url.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
        return sub.url
    
    if getattr(sub, "is_gallery", False):
        items = sub.gallery_data["items"]
        first_id = items[0]["media_id"]
        m = sub.media_metadata[first_id]
        if "s" in m and "u" in m["s"]:
            return m["s"]["u"].replace("&amp;","&")
    
    try:
        return sub.preview["images"][0]["source"]["url"].replace("&amp;","&")
    except Exception:
        return None


# results in list
rows = []
for sr, kw_list in SEARCH_PLAN.items():
    for kw in kw_list:
        for s in tqdm(reddit.subreddit(sr).search(kw, limit=30), desc=f"{sr} - {kw}"):
            img = extract_image(s)
            if not img:
                continue
            rows.append({
                "platform":"reddit",
                "subreddit_board": "r/"+ sr,
                "keyword": kw,
                "source_url":"https://reddit.com"+s.permalink,
                "image_url": img,
                "title": s.title,
                "topic":"wedding",
                "region_culture":"",
                "notes": f"subreddit={sr}; score={s.score}; comments={s.num_comments}",
                "created_utc": int(s.created_utc),
                "created_iso": datetime.fromtimestamp(s.created_utc, timezone.utc).isoformat()
            })


# exporting as csv
df = pd.DataFrame(rows)
df = df.drop_duplicates(subset=["image_url"])
df.to_csv("reddit_samples.csv", index=False, encoding="utf-8")
print(f"Saved {len(df)} unique posts to reddit_samples.csv")
