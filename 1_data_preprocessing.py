import pandas as pd
import re
import string
import emoji

# Load your CSV
df = pd.read_csv("youtube_comments.csv")

def clean_text(text):
    text = str(text).lower()  # lowercase
    
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    
    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)
    
    # Remove mentions and hashtags
    text = re.sub(r"[@#]\S+", "", text)
    
    # Remove emojis
    text = emoji.replace_emoji(text, replace='')
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespaces, newlines, tabs
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

# Apply cleaning to the comment_text column
df['comment_text'] = df['comment_text'].apply(clean_text)

# Save cleaned CSV
df.to_csv("cleaned_comments.csv", index=False, encoding='utf-8')

print("Comments cleaned and saved to cleaned_comments.csv")