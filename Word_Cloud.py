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
