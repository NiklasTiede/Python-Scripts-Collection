# This script generates a word cloud of my linux-cheatsheet and a python logo mask

from wordcloud import WordCloud, STOPWORDS
import sys
import os
import numpy as np
from PIL import Image

# os.chdir(sys.path[0])

text = open('wordcount_CheatSheet.md', mode='r', encoding='utf-8').read()

stopwords = STOPWORDS
stopwords.add('kbd')
stopwords.add('file')

python_mask = np.array(Image.open("python_snakes_mask.png"))

wc = WordCloud(
    background_color="rgba(22, 25, 28, 255)", mode="RGBA",       # colored background
    # background_color="rgba(255, 255, 255, 0)", mode="RGBA",    # gives transparent background
    stopwords=stopwords,
    mask=python_mask
    # height=600,                                                # useful when using no mask
    # width=900,
)

wc.generate(text)

wc.to_file('wordcloud_dark_test.png')

# the image creation can take several seconds!
