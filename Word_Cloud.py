import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
df = pd.read_csv("testdata/Corona_NLP_test.csv", index_col=0)
counter = 0
for index, data in df.iterrows():
    if counter == 5:
        break
    try:
        print(index)
        print(data)
    except:
        print("Exception occurred at", index)
    counter += 1
# Create and generate a word cloud image:
comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.OriginalTweet:

    # typecast each val to string
    val = str(val)

    # split the value
    tokens = val.split()
    for sub_tokens in tokens:
        if "https://t.co/" in sub_tokens:
            tokens.remove(sub_tokens)
        if "Coronavirus" in sub_tokens:
            tokens.remove(sub_tokens)
        if "COVID" in sub_tokens:
            tokens.remove(sub_tokens)
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
