
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys
import os
import numpy as np
from PIL import Image


os.chdir(sys.path[0])

text = open('linux-CheatSheet.md', mode='r', encoding='utf-8').read()

stopwords = STOPWORDS
stopwords.add('kbd')
stopwords.add('file')

python_mask = np.array(Image.open("pysym2.png"))


# background_color="rgba(255, 255, 255, 0)", mode="RGBA"
wc = WordCloud(
    background_color="rgba(22, 25, 28, 255)", mode="RGBA",
    # background_color="rgba(255, 255, 255, 0)", mode="RGBA",
    stopwords=stopwords,
    height=600,
    width=900,
    mask=python_mask
)

wc.generate(text)

# store to file

wc.to_file('wordc3.png')



