###### Seniment analysis

import pandas as pd
from transformers import pipeline, RobertaTokenizer

# Load your CSV file (path to your CSV)
file_path = r'C:/Users/data.csv'

# Read the CSV file
posts_df = pd.read_csv(file_path)

# Extract posts
posts = posts_df['COMBINED'].tolist()

# Use Hugging Face's pipeline for emotion classification (using an emotion-detection model)
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Initialize the tokenizer for RoBERTa to ensure truncation
tokenizer = RobertaTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")

# Function to truncate the text to fit the model's token limit (512 tokens)
def truncate_text(text, max_length=512):
    # Tokenize the text and truncate it if necessary
    tokens = tokenizer(text, truncation=True, max_length=max_length, padding=False)
    return tokenizer.decode(tokens['input_ids'], skip_special_tokens=True)

# List to store results
all_emotions = []
all_confidences = []

# Process posts in batches (optional for larger datasets)
batch_size = 50
for i in range(0, len(posts), batch_size):
    batch_posts = posts[i:i+batch_size]
    
    # Get emotions for each post
    for post in batch_posts:
        truncated_post = truncate_text(post)  # Truncate long posts
        result = classifier(truncated_post)
        emotion_label = result[0]['label']  # Emotion label (joy, sadness, anger, etc.)
        emotion_score = result[0]['score']  # Confidence score
        
        all_emotions.append(emotion_label)
        all_confidences.append(emotion_score)

# Add the emotions and scores to the DataFrame
posts_df['Emotion'] = all_emotions
posts_df['Confidence Score'] = all_confidences

# Save the updated DataFrame to a new CSV file
output_file = r'C:/Users/Sentiment_Analysis.csv'
posts_df.to_csv(output_file, index=False)

# Display the results (optional)
print(posts_df)

