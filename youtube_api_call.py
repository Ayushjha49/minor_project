from googleapiclient.discovery import build
import pandas as pd

# 🔹 Replace with your own API key
API_KEY = "AIzaSyDskPtaOtZCEjePj1zyimqzU2mqfqLVMIQ"

# 🔹 Replace with the video ID you want
VIDEO_ID = "jh66Pjtqr4k"

# Create YouTube API object
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_comments(video_id, max_comments=200):
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        )
        response = request.execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return comments

# Fetch comments
comments = get_comments(VIDEO_ID, max_comments=2000)

# Save to CSV
df = pd.DataFrame(comments, columns=["comment"])
df.to_csv("youtube_comments.csv", index=False)

print(f"Fetched {len(comments)} comments and saved to youtube_comments.csv")