from wordcloud import WordCloud
import matplotlib.pyplot as plt

import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'text1.txt'

text = open(filename).read()

wc = WordCloud().generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()